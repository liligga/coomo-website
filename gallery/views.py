from django.shortcuts import render
from rest_framework import generics
from .models import Gallery, GalleryImage
from .serializers import GalleryDetailSerilizer

# class GalleryListView(generics.ListAPIView):
# 	queryset = Course.objects.all()
# 	serializer_class = 

class CourseDetailView(generics.RetrieveAPIView):
	queryset = Gallery.objects.all()
	serializer_class = GalleryDetailSerilizer