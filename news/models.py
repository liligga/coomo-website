from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import imghdr
from PIL import Image
from pytils.translit import slugify
from django.template.defaultfilters import truncatewords



class News(models.Model):
	LANGUAGE = [
		(None, 'Выберите язык'),
		('Ru', 'Русский'),
		('Kg', 'Кыргызский'), 
		('En', 'Английский'),

	]

	title = models.CharField(max_length=250, verbose_name='Заголовок')
	slug = models.SlugField(blank=True, null=True, unique = True)
	article = RichTextUploadingField(verbose_name='Статья')
	excerpt = models.TextField(blank=True, null=True, verbose_name='Отрывок из статьи')
	important = models.BooleanField(default = False, verbose_name='Важное')
	language = models.CharField(max_length=15, choices=LANGUAGE, verbose_name='Язык')
	author = models.ForeignKey(User, default=True, on_delete=models.CASCADE, verbose_name='Автор')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
	cover = models.ImageField(upload_to='news', verbose_name='Обложка новости')
	banners = models.BooleanField(default=False, verbose_name='Баннер')

	def __str__(self):
		return self.title 

	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		self.excerpt = truncatewords(self.article, 35)
		super(News, self).save(*args, **kwargs)


	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'

# @receiver(post_save, sender=News)
# def image_post_save(sender, instance, *args, **kwargs):
# 	if instance.banners:
# 		preview_cover = Image.open(instance.cover)
# 		extension = imghdr.what(instance.cover)
# 		cover_size = (200, 350)
# 		preview_cover.thumbnail(cover_size)
# 		preview_cover.save(f'{instance.cover}-resized'+extension)
# 	# if created:
# 	# 	new_news = News.objects.get_or_create(news=instance)

# post_save.connect(image_post_save, sender=News)

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
