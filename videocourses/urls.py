from django.urls import path
from .views import CourseListView, CourseDetailView


urlpatterns = [
	path('api/courses', CourseListView.as_view(), name="course_list"),
	path(
		'api/courses/<int:pk>/',
		CourseDetailView.as_view(), name="course_detail"),
]
