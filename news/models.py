from django.db import models
import os
from io import BytesIO
from django.core.files import File
from django.dispatch import receiver
from pathlib import Path
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import imghdr
from PIL import Image
from pytils.translit import slugify
from django.template.defaultfilters import truncatewords
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent



class News(models.Model):
	LANGUAGE = [
		(None, 'Выберите язык'),
		('Ru', 'Русский'),
		('Kg', 'Кыргызский'), 
	]

	title = models.CharField(max_length=250, verbose_name='Заголовок')
	slug = models.SlugField(blank=True, null=True, unique = True, editable = False)
	article = RichTextUploadingField(verbose_name='Статья')
	excerpt = models.TextField(blank=True, null=True, verbose_name='Отрывок из статьи', editable = False)
	important = models.BooleanField(default = False, verbose_name = 'Важное')
	language = models.CharField(max_length=15, choices=LANGUAGE, verbose_name = 'Язык', default='Ru')
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Автор', editable = False)
	created = models.DateTimeField(auto_now_add=True, verbose_name = 'Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name = 'Обновлено')
	cover = models.ImageField(upload_to='news', verbose_name='Обложка новости')
	thumbnail = models.ImageField(upload_to='news', blank=True, null=True, help_text='Заполняется автоматически', verbose_name='Баннер новости')
	banners = models.BooleanField(default=False, verbose_name='Поставить обложку в баннер')

	def __str__(self):
		return self.title 
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		self.excerpt = truncatewords(self.article, 35)
		if self.banners:
			self.thumbnail = self.make_thumbnail(self.cover)
		super(News, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'

	def make_thumbnail(self, cover, size=(200,350)):
		img = Image.open(cover)
		img.thumbnail(size)
		thumb_io = BytesIO()
		img.save(thumb_io, 'JPEG', quality=85)
		thumbnail = File(thumb_io, name=cover.name)
		return thumbnail


def news_pre_save(sender, instance, *args, **kwargs):
	if instance.important:
		try:
			important_news = News.objects.get(important=True)
			if instance != important_news:
				important_news.important = False
				important_news.save()
		except News.DoesNotExist:
			pass


pre_save.connect(news_pre_save, sender=News)
