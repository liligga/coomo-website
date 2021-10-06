from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from .serializers import CoursesListSerializer, CourseDetailSerializer, VideoSerializer


class CourseListView(generics.ListAPIView):
	queryset = Course.objects.all()
	serializer_class = CoursesListSerializer
	filter_backends = [DjangoFilterBackend] #http://*?lang_course=En должно быть после всей ссылки, course_list?lang_course=En 
	filterset_fields = ['lang_course']


class CourseDetailView(generics.RetrieveAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseDetailSerializer