from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import NewsSerializer, NewsDetailSerializer, ImportantNewsSerializer
from menu.models import MenuLink, FooterLink
from menu.serializers import MenuSerializer, FooterSerializer
from reports.models import Reports
from reports.serializers import ReportsSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'


class HomeView(APIView):
    def get(self, request):
        lang = request.META.get('HTTP_ACCEPT_LANGUAGE').capitalize()
        last_eight_news = News.objects.order_by('-created').filter(project=False, lang=lang)[:8]
        important_news = News.objects.filter(important=True, project=False).first()
        banners = News.objects.filter(banners=True, project=False, lang=lang)
        menu = MenuLink.objects.filter(is_active=True, lang=lang)
        reports = Reports.objects.all()
        footer = FooterLink.objects.filter(is_active=True, lang=lang)
        serializer1 = NewsSerializer(last_eight_news, many=True)
        serializer2 = ImportantNewsSerializer(important_news)
        serializer3 = NewsSerializer(banners, many=True)
        serializer4 = MenuSerializer(menu, many=True)
        serializer5 = ReportsSerializer(reports, many=True)
        serializer6 = FooterSerializer(footer, many=True)
        context = {
            'last_eight_news': serializer1.data,
            'important_news': serializer2.data,
            'banners': serializer3.data,
            'menu': serializer4.data,
            'reports': serializer5.data,
            'footer': serializer6.data
        }
        return Response(context)


class NewsListView(ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        lang = self.request.META.get('HTTP_ACCEPT_LANGUAGE', 'Ru').capitalize()
        queryset = News.objects.filter(project=False, lang=lang)
        return queryset

    def list(self, request, *args, **kwargs):
        lang = self.request.META.get('HTTP_ACCEPT_LANGUAGE').capitalize()
        response = super(NewsListView, self).list(request, args, kwargs)
        important_data = News.objects.filter(important=True, project=False).first()
        important_news = ImportantNewsSerializer(important_data)
        response.data['important_news'] = important_news.data
        return response


class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        lang = self.request.META.get('HTTP_ACCEPT_LANGUAGE').capitalize()
        current = News.objects.get(slug=kwargs.get('slug'))
        current_news = NewsDetailSerializer(current)
        important_data = News.objects.filter(important=True, project=False).first()
        important_news = ImportantNewsSerializer(important_data)
        four_last_news = News.objects.all().exclude(id=current.id).order_by('-id').filter(project=False, lang=lang)[:4]
        four_last_news = NewsSerializer(four_last_news, many=True)
        return Response({'current_news': current_news.data, 'related': four_last_news.data,
                         'important_news': important_news.data, })


class ProjectList(ListAPIView):
    queryset = News.objects.filter(project=True)
    serializer_class = NewsSerializer
    pagination_class = CustomPagination

# class ProjectDetailView(RetrieveAPIView):
#     queryset = News.objects.filter(project=True)
#     serializer_class = NewsDetailSerializer
#     lookup_field = 'slug'
