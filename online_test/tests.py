from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import OnlineTest
from .factories import *
from .serializers import *


class TestOnlineTest(APITestCase):
	def setUp(self):
		self.test_list = OnlineTestFactory.create_batch(5)

	def test_online_test_list(self):
		response = self.client.get(reverse('onlinetest-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 5)
		serializer_data = OnlineTestListSerializer(self.test_list, many=True)
		self.assertEqual(serializer_data.data, response.data)

	def test_questions_test(self):
		response = self.client.get(reverse('online_tests-questions', kwargs={'pk': self.test_list[0].id}))
		serializer_data = QuestionSerializer(self.test_list[0]).data['questions']
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertQuerysetEqual(serializer_data, response.data['questions'])

	def test_answer_right(self):
		response = self.client.get(reverse('online_tests-answers', kwargs={'pk': self.test_list[0].id}))
		right_answer = {1: 'А'}
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(right_answer, response.data['answers'])


	def test_answer_is_not_right(self):
		response = self.client.get(reverse('online_tests-answers', kwargs={'pk': self.test_list[0].id}))
		right_answer = {1: 'Б'}
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertNotEqual(right_answer, response.data['answers'])