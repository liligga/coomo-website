from django.shortcuts import render
# from django.views.generic import ListView
from .models import *
from rest_framework.response import Response
from rest_framework import generics
# from rest_framework.views import ListAPIView
from .serializers import CoursesListSerializer, CourseDetailSerializer


class CourseListView(generics.ListAPIView):
	queryset = Course.objects.all()
	serializer_class = CoursesListSerializer


class CourseDetailView(generics.RetrieveAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseDetailSerializer