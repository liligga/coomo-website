from django.test import TestCase, Client
from django.urls import reverse

from faq.models import FAQ


class TestFAQ(TestCase):
    def setUp(self):
        self.client = Client()

        self.faq1 = FAQ.objects.create(question='Вопрос', answer='Ответ')
        self.faq1.save()
        self.faq2 = FAQ.objects.create(question='Вопрос2', answer='Ответ2')
        self.faq2.save()

        self.list_url = reverse('faq_list')

        return super().setUp()

    def test_faq_list(self):
        response = self.client.get(self.list_url)
        data = [
            {
                "id": 1,
                "question": "Вопрос",
                "answer": "Ответ"
            },

            {
                "id": 2,
                "question": "Вопрос2",
                "answer": "Ответ2"
            },
        ]


        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(data, response.json())
