from django.shortcuts import render
from rest_framework import generics
from .models import Gallery
from .serializers import GalleryDetailSerilizer, GalleryListSerializers

class GalleryListView(generics.ListAPIView):
	queryset = Gallery.objects.all()
	serializer_class = GalleryListSerializers

class GalleryDetailView(generics.RetrieveAPIView):
	queryset = Gallery.objects.all()
	serializer_class = GalleryDetailSerilizer

