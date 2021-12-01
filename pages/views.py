from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from news.views import CustomPagination
from pages.models import Page
from pages.serializers import PageSerializer, PageListSerializer


class PageListView(ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageListSerializer
    # pagination_class = CustomPagination


class PageDetailView(RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'
