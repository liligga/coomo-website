from rest_framework import generics
from .models import Gallery
from .serializers import GalleryDetailSerilizer, GalleryListSerializers
from rest_framework.pagination import PageNumberPagination
from news.views import CustomPagination


class GalleryListView(generics.ListAPIView):
	queryset = Gallery.objects.all()
	serializer_class = GalleryListSerializers
	pagination_class = CustomPagination


class GalleryDetailView(generics.RetrieveAPIView):
	queryset = Gallery.objects.all()
	serializer_class = GalleryDetailSerilizer
