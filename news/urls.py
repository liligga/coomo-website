from django.urls import path
from .views import HomeView, NewsDetailView, NewsListView, ProjectList

urlpatterns = [
	path('api/home', HomeView.as_view(), name='home'),
	path('api/news', NewsListView.as_view(), name='news_list'),
	path('api/news/<str:slug>', NewsDetailView.as_view(), name="news_detail"),
	path('api/projects', ProjectList.as_view(), name='project_list'),
	# path('api/projects/<str:slug>', ProjectDetailView.as_view(), name='project_detail')
]
