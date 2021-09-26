from django.db import models
from django.contrib.auth.models import User
from django.utils.text import  slugify



class News(models.Model):
	LANGUAGE = [
		('ru', 'Русский'),
		('kg', 'Кыргызский'),
	]

	title = models.CharField(max_length=250, verbose_name='Заголовок')
	slug = models.SlugField(unique=True, help_text='Выберите язык')
	text = models.TextField(verbose_name='Текст')
	language = models.CharField(max_length=15, choices=LANGUAGE, verbose_name='Язык')
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
	image = models.ImageField(upload_to='images', blank=True, verbose_name='Картинка')
	

	def __str__(self):
		return self.title


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(News, self).save(*args, **kwargs)


	class Meta:
		verbose_name='Новость'
		verbose_name_plural='Новости'

