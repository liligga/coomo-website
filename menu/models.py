from django.db import models

from news.models import News

LANGUAGE_CHOICES = [
	('Ru', 'Русский'),
	('Kg', 'Кыргызский'),
]


class ActiveLinksManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class MenuLink(models.Model):
	title = models.CharField(max_length=100, verbose_name='Название')
	is_active = models.BooleanField(default=False, verbose_name='Активно')
	link = models.URLField(max_length=200, verbose_name='Ссылка', blank=True, null=True)
	icon = models.FileField(
		upload_to='icons_menu',
		unique=True,
		help_text="Добавлять только картинки размера 25х25",
		verbose_name='Иконка',
		blank=True,
		null=True)
	lang = models.CharField(
		max_length=15,
		choices=LANGUAGE_CHOICES,
		default='Ru',
		verbose_name='Язык',
		blank=True,
		null=True)
	news = models.ForeignKey(
		News,
		blank=True,
		null=True,
		on_delete=models.DO_NOTHING,
		help_text='Укажите новость, если ссылка должна указывать на неё',
		verbose_name='Связанная новость',
		related_name='news_link')
	objects = models.Manager()
	active_objects = ActiveLinksManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Ссылка в меню'
		verbose_name_plural = 'Ссылки меню'


class FooterLink(models.Model):
	title = models.CharField(max_length=100)
	is_active = models.BooleanField(default=False)
	link = models.URLField(max_length=200)
	lang = models.CharField(
		max_length=15,
		choices=LANGUAGE_CHOICES,
		default='Ru')

	objects = models.Manager()
	active_objects = ActiveLinksManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Ссылка футера'
		verbose_name_plural = 'Ссылки футера'
