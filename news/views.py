from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import NewsListSerializer, NewsDetailSerializer


class NewsListView(generics.ListAPIView):
	queryset = News.objects.all()
	serializer_class = NewsListSerializer


class NewsDetailView(generics.RetrieveAPIView):
	queryset = News.objects.all()
	serializer_class = NewsDetailSerializer

