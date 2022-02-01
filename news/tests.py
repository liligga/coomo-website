from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import *
from .serializers import *
from .views import *
from .factories import *
from urllib.parse import urlencode
from django.test import Client


class TestNews(APITestCase):
    def setUp(self):
        self.client = Client(HTTP_ACCEPT_LANGUAGE='Ru')
        self.news_list = NewsFactory.create_batch(4)

    def test_news_home(self):
        header = {'Accept-Language': 'ru'}
        response = self.client.get(reverse('home'), content_type='application/json', **header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['last_eight_news']), 4)
        serializer_data = NewsSerializer(self.news_list, many=True)
        self.assertEqual(serializer_data.data, response.data['last_eight_news'][::-1])

    def test_news_detail(self):
        header = {'Accept-Language': 'ru'}
        response = self.client.get(reverse('news_detail', kwargs={'slug': self.news_list[0].slug}), content_type='application/json', **header)
        serializer_data = NewsDetailSerializer(self.news_list[0]).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data.get('current_news'))
