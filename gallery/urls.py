from django.urls import path
from .views import GalleryDetailView, GalleryListView

urlpatterns = [
	path('api/galleries', GalleryListView.as_view(), name='gallery_list'),
	path('api/galleries/<int:pk>', GalleryDetailView.as_view(), name='gallery_detail'),
]