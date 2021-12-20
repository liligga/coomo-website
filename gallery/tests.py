from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Gallery, GalleryImage
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import json
import os


class TestGallery(APITestCase):
	def setUp(self):
		self.user = User.objects.create(username='testadmin', password='testpassword')
		self.test_gallery_one = Gallery.objects.create(
			title='test title',
			description='test description',
			author=self.user)
		self.test_gallery_two = Gallery.objects.create(
			title='test title 2',
			description='test description 2',
			author=self.user)
		self.test_gallery_images_one = GalleryImage.objects.create(
			gallery_id=self.test_gallery_one,
			photo=SimpleUploadedFile(
				name='test_image_one.jpg',
				content=b'',
				content_type='image/jpeg'))
		self.test_gallery_images_two = GalleryImage.objects.create(
			gallery_id=self.test_gallery_two,
			photo=SimpleUploadedFile(
				name='test_image_two.jpg',
				content=b'',
				content_type='image/jpeg'))

	def tearDown(self):
		if os.path.exists(self.test_gallery_images_one.photo.path):
			os.remove(self.test_gallery_images_one.photo.path)
			os.remove(self.test_gallery_images_two.photo.path)

	def test_gallery_list(self):
		response = self.client.get(reverse('gallery_list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 4)
		self.assertTrue([{
			'id': self.test_gallery_one.id,
			'title': self.test_gallery_one.title,
			'photo': self.test_gallery_images_one.photo
			}, {
			'id': self.test_gallery_two.id,
			'title': self.test_gallery_two.title,
			'photo': self.test_gallery_images_two.photo}]) in response.json()

	def test_gallery_detail(self):
		response = self.client.get(reverse('gallery_detail', kwargs={'pk':'1'}))
		data = json.loads(response.content)
		content = {
				'id': self.test_gallery_one.id,
				'title': self.test_gallery_one.title,
				'photos_gallery': [{'photo': self.test_gallery_images_one.photo}]}
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(data, content)
