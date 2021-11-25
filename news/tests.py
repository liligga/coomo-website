from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from .views import *
from menu.models import MenuLink


class TestNews(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testadmin', password='testpassword')
        self.test_news = News.objects.create(
            title='Testnews',
            slug='testnews',
            article='Intro test text',
            excerpt='Test News',
            important=True,
            lang='Ru',
            author=self.user,
            cover='test_image.jpg',
            banners=True,
        )
        self.test_news_kg = News.objects.create(
            title='Kg Testnews',
            slug='kg-testnews',
            article='Kg Intro test text',
            excerpt='Kg Test News',
            important=False,
            lang='Kg',
            author=self.user,
            cover='test_image.jpg',
            banners=True,
        )
        self.test_news_with_parent_ru = News.objects.create(
            title='Kg Testnews1',
            slug='kg-testnews1',
            article='Kg Intro test text1',
            excerpt='Kg Test News1',
            important=True,
            lang='Kg',
            author=self.user,
            cover='test_image1.jpg',
            banners=True,
            parent=self.test_news
        )
        self.test_menu = MenuLink.objects.create(
			title='Test Menu Ru',
			is_active=True,
			link='https://www.vk.com/',
			icon='test_icon_active.jpg',
			lang='Ru')

    def test_news_list(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertTrue({"last_eight_news": [
                            {'id': 3,
                                'title': 'Kg Testnews1',
                                'slug': 'kg-testnews1',
                                'article': 'Kg Intro test text1',
                                'excerpt': 'Kg Test News1',
                                'lang': 'Kg',
                                'cover': 'test_image1.jpg'},
                            {'id': 2,
                                'title': 'Kg Testnews',
                                'slug': 'kg-testnews',
                                'article': 'Kg Intro test text',
                                'excerpt': 'Kg Test News',
                                'lang': 'Kg',
                                'cover': 'test_image.jpg'},
                            {'id': 1,
                                'title': 'Testnews',
                                'slug': 'testnews',
                                'article': 'Intro test text',
                                'excerpt': 'Test News',
                                'lang': 'Ru',
                                'cover': 'test_image.jpg'}
                            ],
                        "important_news": [
                            {'id': 1,
                                'title': 'Testnews',
                                'slug': 'testnews',
                                'article': 'Intro test text',
                                'excerpt': 'Test News',
                                'lang': 'Ru',
                                'cover': 'test_image.jpg'},
                            {'id': 3,
                                'title': 'Kg Testnews1',
                                'slug': 'kg-testnews1',
                                'article': 'Kg Intro test text1',
                                'excerpt': 'Kg Test News1',
                                'lang': 'Kg',
                                'cover': 'test_image1.jpg'}							
                        ],
                        "banners": [
                            {'id': 1,
                                'title': 'Testnews',
                                'slug': 'testnews',
                                'article': 'Intro test text',
                                'excerpt': 'Test News',
                                'lang': 'Ru',
                                'cover': 'test_image.jpg'},
                            {'id': 2,
                                'title': 'Kg Testnews',
                                'slug': 'kg-testnews',
                                'article': 'Kg Intro test text',
                                'excerpt': 'Kg Test News',
                                'lang': 'Kg',
                                'cover': 'test_image.jpg'},
                            {'id': 3,
                                'title': 'Kg Testnews1',
                                'slug': 'kg-testnews1',
                                'article': 'Kg Intro test text1',
                                'excerpt': 'Kg Test News1',
                                'lang': 'Kg',
                                'cover': 'test_image1.jpg'}
                        ],
                        "menu": [
                            {'id': 1,
                                'title': 'Test Menu Ru',
                                'link': 'https://www.vk.com/',
                                'icon': self.test_menu.icon,
                                'lang': 'Ru'
                            }]}) in response.json()

    # def test_news_detail(self):
    #     response = self.client.get(reverse('news_detail', kwargs={'slug': self.test_news.slug}))
    #     serializer_data = NewsDetailSerializer(self.test_news).data
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(serializer_data, response.data.get('current_news'))
