from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import NewsLastestSerializer, NewsImportantSerializer, NewsBannerSerializer


class NewsView(APIView):	
	def get(self, request):
		last_eight_news = News.objects.order_by('-created')[:8]
		important_news = News.objects.filter(important=True)
		banners = News.objects.all()
		serializer1 = NewsLastestSerializer(last_eight_news, many=True)
		serializer2 = NewsImportantSerializer(important_news, many=True)
		serializer3 = NewsBannerSerializer(banners, many=True)
		context = {'last_eight_news':serializer1.data,
					'important_news':serializer2.data,
					'banners':serializer3.data}

		return Response(context)




class NewsDetailView(APIView):
	def get(self, request):
		news = News.objects.all().latest('id')[:4]
		serializer = NewsSerializer(news)
		return Response (serializer.data)

			