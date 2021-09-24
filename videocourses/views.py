from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from .serializers import CoursesListSerializer, CourseDetailSerializer, VideoSerializer


class CourseListView(generics.ListAPIView):
	queryset = Course.objects.all()
	serializer_class = CoursesListSerializer


class CourseDetailView(generics.RetrieveAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseDetailSerializer