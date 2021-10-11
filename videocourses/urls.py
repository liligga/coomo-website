from django.urls import path
from .views import *
from . import views



urlpatterns = [
	path('api/courses', views.CourseListView.as_view(), name="course_list"),
	path('api/courses/<int:pk>/', views.CourseDetailView.as_view(), name="course_detail"),
]