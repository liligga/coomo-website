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
			lang='Ru')
		self.test_course_kg = Course.objects.create(
			name='Test Course Kyrgyz',
			description='Test description kyrgyz',
			lang='Kg')
		self.test_video = Video.objects.create(
			course=self.test_course,
			name='test_name',
			video_link='https://www.test_link.ru',
			lang='Ru')

	def test_course_list(self):
		response = self.client.get(reverse('course_list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 2)
		self.assertTrue(
			{'id': 1,
				'name': 'Test Course',
				'description': 'Test description',
				'lang': 'Ru'},
			{'id': 2,
				'name': 'Test Course Kyrgyz',
				'description': 'Test description kyrgyz',
				'lang': 'Kg'}) in response.json()

	def test_course_detail(self):
		response = self.client.get(reverse(
			'course_detail',
			kwargs={'pk': self.test_course.id}))
		serializer_data = CourseDetailSerializer(self.test_course).data
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(serializer_data, response.data)
