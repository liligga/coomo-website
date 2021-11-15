from django.urls import path
from .views import NewsView, NewsDetailAPIView

urlpatterns = [
	path('api/news/', NewsView.as_view(), name='news_list'),
	# path('api/news/<int:pk>/', NewsDetailView.as_view(), name="news_detail"),
	path('api/news/', NewsView.as_view(), name='news_list'),
	path('api/news/<str:slug>/', NewsDetailAPIView.as_view(), name="news_detail"),
]
