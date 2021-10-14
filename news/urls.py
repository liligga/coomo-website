from django.urls import path
from .views import NewsView, NewsDetailView


urlpatterns = [
	path('api/news/',NewsView.as_view(), name='news_list'),
	path('api/news/<int:pk>/', NewsDetailView.as_view(), name="news_detail"),
]
