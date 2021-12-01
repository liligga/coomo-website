from django.urls import path

from pages.views import PageListView, PageDetailView

urlpatterns = [
    path('api/pages/', PageListView.as_view()),
    path('api/pages/<slug>', PageDetailView.as_view())
]