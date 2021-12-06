from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import MenuLink, FooterLink
from pages.models import Page


class TestMenuFooter(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testadmin', password='testpassword')
        self.test_page = Page.objects.create(
            title='Test Title',
            article='Test Article')
        self.test_page_kg = Page.objects.create(
            title='Test Title Kg',
            article='Test Article Kg')
        self.test_menu_active_ru = MenuLink.objects.create(
            title='Test Menu Ru',
            is_active=True,
            icon='test_icon_active.jpg',
            lang='Ru',
            page=self.test_page)
        self.test_menu_active_kg = MenuLink.objects.create(
            title='Test Menu Kg',
            is_active=True,
            icon='test_icon_active_kg.jpg',
            lang='Kg',
            page=self.test_page_kg)
        self.test_menu_inactive = MenuLink.objects.create(
            title='Test Menu Ru',
            is_active=False,
            icon='test_icon_inactive.jpg',
            lang='Ru',
            page=self.test_page)
        self.test_footer_active_ru = FooterLink.objects.create(
            title='Test Footer Ru',
            is_active=True,
            link='https://www.instagram.com/',
            lang='Ru')
        self.test_footer_active_kg = FooterLink.objects.create(
            title='Test Footer Kg',
            is_active=True,
            link='https://www.instagram.com/',
            lang='Kg')
        self.test_footer_inactive = FooterLink.objects.create(
            title='Test Footer Ru',
            is_active=False,
            link='https://www.instagram.com/',
            lang='Ru')

    def test_menu_list(self):
        response = self.client.get(reverse('menu_objects'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertTrue(
            {'id': 1,
                'title': 'Test Menu Ru',
                'icon': self.test_menu_active_ru.icon,
                'lang': 'Ru',
                'page': self.test_page
            }) in response.json()

    def test_menu_list_filtered_kg(self):
        response = self.client.get(reverse('menu_objects') + '?lang=Kg')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertTrue(
            {'id': 2,
                'title': 'Test Menu Kg',
                'icon': self.test_menu_active_kg.icon,
                'lang': 'Kg',
                'page': self.test_page_kg
            }) in response.json()

    def test_footer_list(self):
        response = self.client.get(reverse('footer_objects'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertTrue(
            {'id': 1,
                'title': 'Test Footer Ru',
                'link': 'https://www.instagram.com/',
                'lang': 'Ru'
            }) in response.json()

    def test_footer_list_filtered_kg(self):
        response = self.client.get(reverse('footer_objects') + '?lang=Kg')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertTrue(
            {'id': 2,
                'title': 'Test Footer Kg',
                'link': 'https://www.instagram.com/',
                'lang': 'Kg'
            }) in response.json()
