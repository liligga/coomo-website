from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import NewsListSerializer, NewsDetailSerializer


class NewsListView(generics.ListAPIView):
	queryset = News.objects.all()[:8]
	serializer_class = NewsListSerializer
	filter_backends = [DjangoFilterBackend] 
	filterset_fields = ['important']



class NewsDetailView(generics.RetrieveAPIView):
	queryset = News.objects.all()
	serializer_class = NewsDetailSerializer

