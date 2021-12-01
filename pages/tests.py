from django.test import TestCase, Client
from django.urls import reverse

from pages.models import Page


class TestPages(TestCase):
    def setUp(self):
        self.client = Client()

        self.page1 = Page.objects.create(title='Студентам', article='Информация для студентов')
        self.page2 = Page.objects.create(title='Абитуриентам', article='Информация для абитуриентов')
        self.page3 = Page.objects.create(title='Учителям', article='Информация для учителей')

        self.list_url = reverse('pages_list')
        self.detail_url = reverse('pages_detail', args=(self.page1.slug,))

        return super().setUp()

    def test_pages_list(self):
        response = self.client.get(self.list_url)

        data = [
            {
                'id': self.page1.id,
                'title': 'Студентам',
                'slug': 'studentam'
            },
            {
                'id': self.page2.id,
                'title': 'Абитуриентам',
                'slug': 'abiturientam'
            },
            {
                'id': self.page3.id,
                'title': 'Учителям',
                'slug': 'uchitelyam'
            },
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(data, response.json())

    def test_pages_detail(self):
        response = self.client.get(self.detail_url)

        data = {
            'id': 1,
            'title': 'Студентам',
            'slug': 'studentam',
            'article': 'Информация для студентов'
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, response.json())
