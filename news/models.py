from django.db import models
from django.contrib.auth.models import User
from django.utils.text import  slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from django.dispatch import receiver



class News(models.Model):
	LANGUAGE = [
		(None, 'Выберите язык'),
		('ru', 'Русский'),
		('kg', 'Кыргызский'),
	]

	title = models.CharField(max_length=250, verbose_name='Заголовок')
	slug = models.SlugField(unique=True)
	text = RichTextUploadingField(verbose_name='Текст')
	impotant = models.BooleanField(default = False, verbose_name = 'Важное')
	language = models.CharField(max_length=15, choices=LANGUAGE, verbose_name='Язык')
	author = models.ForeignKey(User, default=True, on_delete=models.CASCADE, verbose_name='Автор')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
	updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
	
	

	def __str__(self):
		return self.title


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(News, self).save(*args, **kwargs)


	class Meta:
		verbose_name='Новость'
		verbose_name_plural='Новости'


def news_pre_save(sender, instance, *args, **kwargs):
        if instance.impotant:
            try:
                impotant_news = News.objects.get(impotant=True)
                if instance != impotant_news:
                    impotant_news.impotant = False
                    impotant_news.save()
            except News.DoesNotExist:
            	pass
                
pre_save.connect(news_pre_save, sender=News)




