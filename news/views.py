from django.db.models import query
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import NewsSerializer, NewsDetailSerializer
from menu.models import MenuLink
from menu.serializers import MenuSerializer
from reports.models import Reports
from reports.serializers import ReportsSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'


class HomeView(APIView):
    def get(self, request):
        last_eight_news = News.objects.order_by('-created')[:8]
        important_news = News.objects.filter(important=True)
        banners = News.objects.filter(banners=True)
        menu = MenuLink.objects.filter(is_active=True)
        reports = Reports.objects.all()
        serializer1 = NewsSerializer(last_eight_news, many=True)
        serializer2 = NewsSerializer(important_news, many=True)
        serializer3 = NewsSerializer(banners, many=True)
        serializer4 = MenuSerializer(menu, many=True)
        serializer5 = ReportsSerializer(reports, many=True)
        context = {
            'last_eight_news': serializer1.data,
            'important_news': serializer2.data,
            'banners': serializer3.data,
            'menu': serializer4.data,
            'reports': serializer5.data
        }
        return Response(context)


class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        current = News.objects.get(slug=kwargs.get('slug'))
        current_news = NewsDetailSerializer(current)
        four_last_news = News.objects.all().exclude(id=current.id).order_by('-id')[:4]
        four_last_news = NewsDetailSerializer(four_last_news, many=True)
        return Response({'current_news': current_news.data, 'related': four_last_news.data})
