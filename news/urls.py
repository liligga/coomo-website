from django.urls import path
from . import views


urlpatterns = [
	path('api/news/', views.NewsListView.as_view(), name='news_list'),
	# path('api/news/<int:pk>/', views.NewsDetailView.as_view(), name="news_detail"),
]
