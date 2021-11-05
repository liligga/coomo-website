from django.urls import path
from .views import CourseDetailView

urlpatterns = [
	path('api/gallery/<int:pk>', CourseDetailView.as_view(), name='gallery_detail')
]