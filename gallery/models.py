from django.db import models
import os
from django.contrib.auth.models import User


def get_upload_to(instance, filename):
	return os.path.join('gallery', f'{instance.gallery_id.id}', filename)


class Gallery(models.Model):
	title = models.CharField(max_length=150, verbose_name='Название галлереи')
	description = models.TextField(blank=True, null=True, verbose_name='Описание галлереи')
	author = models.ForeignKey(
		User,
		default=True,
		on_delete=models.CASCADE,
		verbose_name='Автор')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Галлерея'
		verbose_name_plural='Галлереи'


class GalleryImage(models.Model):
	gallery_id = models.ForeignKey(
		Gallery,
		on_delete=models.CASCADE,
		verbose_name='Имя галлереи',
		help_text='Выберите к какой галлерее будет принадлежать картинки',
		related_name='photos')
	photo = models.ImageField(upload_to=get_upload_to, verbose_name='Картинка')

	class Meta:
		verbose_name='Картинка в галлерее'
		verbose_name_plural='Картинки в галлерее'

	def __str__(self):
		return ''

	def photo_url(self):
		return self.photo.url