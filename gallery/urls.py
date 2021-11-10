from django.urls import path
from .views import GalleryDetailView, GalleryListView

urlpatterns = [
	path('api/gallery_list', GalleryListView.as_view(), name='gallery_list'),
	path('api/gallery/<int:pk>', GalleryDetailView.as_view(), name='gallery_detail'),
]