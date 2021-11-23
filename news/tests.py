# from rest_framework.test import APITestCase
# from django.urls import include, path, reverse
# from django.urls import reverse
# from rest_framework import status
# from django.contrib.auth.models import User
# from .models import *
# from .serializers import *
# from .views import *
# from menu.models import MenuLink
# from menu.serializers import MenuSerializer


# class TestNews(APITestCase):
#     def setUp(self):
#         self.test_news = News.objects.create(
#             title='Testnews',
#             slug='testnews',
#             excerpt='Test News',
#             important=True,
#             banners=True,
#         )
#         self.test_menu = MenuLink.objects.create(
#             title='Testmenu',
#             is_active=True)

#         author_test = User.objects.create_user(username='testadmin', password='admin')

#     def test_news_list(self):
#         response = self.client.get(reverse('news_list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 4)
#         self.assertTrue({'id': 1, 'title': 'Testnews', 'slug': 'testnews', 'excerpt': 'Test News'}) in response.json()
#         self.assertTrue({'title': 'Testmenu'}) in response.json()

#     def test_news_detail(self):
#         response = self.client.get(reverse('news_detail', kwargs={'pk': self.test_news.id}))
#         serializer_data = NewsDetailSerializer(self.test_news).data
#         self.assertEqual(serializer_data, response.data.get('current_article'))
