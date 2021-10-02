from django.urls import path
from . import views


urlpatterns = [
	path('api/news_list/', views.NewsListView.as_view(), name='news_list'),
	path('api/news_detail/<int:pk>/', views.NewsDetailView.as_view(), name="news_detail"),
]
