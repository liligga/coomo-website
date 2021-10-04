from django.urls import path
from .views import *
from . import views



urlpatterns = [
	path('api/course_list', views.CourseListView.as_view(), name="course_list"),
	path('api/course_detail/<int:pk>/', views.CourseDetailView.as_view(), name="course_detail"),
]