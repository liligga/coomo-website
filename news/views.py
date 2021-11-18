from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import NewsSerializer, NewsDetailSerializer
from menu.models import MenuLink
from menu.serializers import MenuSerializer


class NewsView(APIView):
    def get(self, request):
        last_eight_news = News.objects.order_by('-created')[:8]
        important_news = News.objects.filter(important=True)
        banners = News.objects.filter(banners=True)
        menu = MenuLink.objects.filter(is_active=True)
        serializer1 = NewsSerializer(last_eight_news, many=True)
        serializer2 = NewsSerializer(important_news, many=True)
        serializer3 = NewsSerializer(banners, many=True)
        serializer4 = MenuSerializer(menu, many=True)
        context = {
            'last_eight_news': serializer1.data,
            'important_news': serializer2.data,
            'banners': serializer3.data,
            'menu': serializer4.data}

        return Response(context)


# class NewsDetailView(generics.RetrieveAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsDetailSerializer
#
#     def retrieve(self, request, *args, **kwargs):
#         result = super(NewsDetailView, self).retrieve(request, *args, **kwargs)
#         four_last_news = News.objects.all()[:4]
#         four_last_news = NewsDetailSerializer(four_last_news, many=True)
#         return Response({'current_article': result.data, 'related': four_last_news.data})
#
#
#     def get(self, request):
#         last_eight_news = News.objects.order_by('-created')[:8]
#         important_news = News.objects.filter(important=True)
#         banners = News.objects.filter(banners=True)
#         menu = MenuLink.objects.filter(is_active=True)
#         serializer1 = NewsSerializer(last_eight_news, many=True)
#         serializer2 = NewsSerializer(important_news, many=True)
#         serializer3 = NewsSerializer(banners, many=True)
#         serializer4 = MenuSerializer(menu, many=True)
#         context = {'last_eight_news': serializer1.data,
#                    'important_news': serializer2.data,
#                    'banners': serializer3.data,
#                    'menu': serializer4.data}
#
#         return Response(context)


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        current = News.objects.get(slug=kwargs.get('slug')).news
        current_news = NewsDetailSerializer(current, many=True)
        four_last_news = News.objects.all().order_by('-id')[:4]
        four_last_news = NewsDetailSerializer(four_last_news, many=True)

        return Response({'current_news': current_news.data, 'related': four_last_news.data})
