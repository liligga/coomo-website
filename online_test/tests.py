from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import OnlineTest


class TestOnlineTest(APITestCase):
	def setUp(self):
		self.test_online_test_math_ru = OnlineTest.objects.create(
			name='Math_ru',
			part_num=1,
			version=2,
			duration=60,
			num_questions=15,
			num_answers=6,
			language='Ru',
			is_active=True,
			intro='Test Text'
		)
		self.test_online_test_analogies_ru = OnlineTest.objects.create(
			name='Analogies_ru',
			part_num=1,
			version=1,
			duration=60,
			num_questions=15,
			num_answers=6,
			language='Ru',
			is_active=True,
			intro='Test Text'
		)
		self.test_online_test_history_kg = OnlineTest.objects.create(
			name='History_kg',
			part_num=2,
			version=3,
			duration=80,
			num_questions=25,
			num_answers=6,
			language='Kg',
			is_active=True,
			intro='Test Text'
		)
		self.test_online_test_history_kg = OnlineTest.objects.create(
			name='History_kg',
			part_num=2,
			version=3,
			duration=80,
			num_questions=25,
			num_answers=6,
			language='Kg',
			is_active=False,
			intro='Test Text'
		)

	def test_online_test_list(self):
		response = self.client.get(reverse('onlinetest-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 4)
		self.assertTrue([{
			'id': 1,
			'name': 'Math_ru',
			'part_num': 1,
			'version': 1,
			'duration': 60,
			'num_answers': 6,
			'language': 'Ru',
			'is_active': True,
			'intro': 'Test Text'
		}, {
			'id': 2,
			'name': 'Analogies_ru',
			'part_num': 1,
			'version': 2,
			'duration': 60,
			'num_answers': 6,
			'language': 'Ru',
			'is_active': True,
			'intro': 'Test Text'
		}, {
			'id': 3,
			'name': 'History_kg',
			'part_num': 2,
			'version': 3,
			'duration': 80,
			'num_answers': 6,
			'language': 'Kg',
			'is_active': True,
			'intro': 'Test Text'
		}, {
			'id': 4,
			'name': 'History_kg',
			'part_num': 2,
			'version': 3,
			'duration': 80,
			'num_answers': 6,
			'language': 'Kg',
			'is_active': False,
			'intro': 'Test Text'}])
