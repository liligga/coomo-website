from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import NewsLastestSerializer, NewsDetailSerializer




class NewsView(APIView):
	def get(self, request):
		last_eight_news = News.objects.order_by('-created')[:8]
		important_news = News.objects.filter(important=True)
		banners = News.objects.filter(banners = True)
		serializer1 = NewsLastestSerializer(last_eight_news, many=True)
		serializer2 = NewsLastestSerializer(important_news, many=True)
		serializer3 = NewsLastestSerializer(banners, many=True)
		context = {'last_eight_news':serializer1.data,
					'important_news':serializer2.data,
					'banners':serializer3.data}

		return Response(context)




class NewsDetailView(generics.RetrieveAPIView):
	queryset = News.objects.all()
	serializer_class = NewsDetailSerializer


	def retrieve(self, request, *args, **kwargs):
		result = super(NewsDetailView, self).retrieve(request, *args, **kwargs)
		four_last_news = News.objects.all()[:4]
		four_last_news = NewsDetailSerializer(four_last_news, many=True)
		return Response({'current_article':result.data, 'related':four_last_news.data})

	