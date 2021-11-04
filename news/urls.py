from django.urls import path
from .views import NewsView, SearchView, NewsDetailAPIView, NewsDetailView

urlpatterns = [
	path('api/news/', NewsView.as_view(), name='news_list'),
	path('api/news/<int:pk>/', NewsDetailView.as_view(), name="news_detail"),
	path('api/news/', NewsView.as_view(), name='news_list'),
	path('api/news/<str:slug>/', NewsDetailAPIView.as_view(), name="news_detail"),
	path('api/search/', SearchView.as_view(), name='search_news'),

]
