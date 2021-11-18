from django.urls import path

from search.views import GlobalSearchList

urlpatterns = [
    path('api/search/', GlobalSearchList.as_view(), name='search_news'),
]
