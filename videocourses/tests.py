from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Course, Video
from .serializers import CourseDetailSerializer


class TestCourse(APITestCase):
	def setUp(self):
		self.test_course = Course.objects.create(
			name='Test Course',
			description='Test description',
			lang_course='Ru')
		self.test_course_en = Course.objects.create(
			name='Test Course English',
			description='Test description english',
			lang_course='En')
		self.test_course_kg = Course.objects.create(
			name='Test Course Kyrgyz',
			description='Test description kyrgyz',
			lang_course='Kg')
		self.test_video = Video.objects.create(
			course=self.test_course,
			name='test_name',
			video_link='https://www.test_link.ru',
			lang_video='Ru')

	def test_course_list(self):
		response = self.client.get(reverse('course_list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 3)
		self.assertTrue(
			{'id': 1,
				'name': 'Test Course',
				'description': 'Test description',
				'lang_course': 'Ru'}) in response.json()

	def test_course_detail(self):
		response = self.client.get(reverse(
			'course_detail',
			kwargs={'pk': self.test_course.id}))
		serializer_data = CourseDetailSerializer(self.test_course).data
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(serializer_data, response.data)

	def test_course_list_filtered_en(self):
		response = self.client.get(reverse('course_list') + '?lang_course=En')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)
		self.assertTrue(
			{'id': 2,
				'name': 'Test Course English',
				'description': 'Test description english',
				'lang_course': 'En'}) in response.json()

	def test_course_list_filtered_kg(self):
		response = self.client.get(reverse('course_list') + '?lang_course=Kg')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)
		self.assertTrue(
			{'id': 3,
				'name': 'Test Course Kyrgyz',
				'description': 'Test description kyrgyz',
				'lang_course': 'Kg'}) in response.json()
