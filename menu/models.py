from django.db import models


LANGUAGE_CHOICES = [
	('Ru', 'Русский'),
	('Kg', 'Кыргызский'),
]


class ActiveLinksManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class MenuLink(models.Model):
	title = models.CharField(max_length=100)
	is_active = models.BooleanField(default=False)
	link = models.URLField(max_length=200)
	icon = models.ImageField(
		upload_to='media/icons_menu',
		unique=True,
		help_text="Добавлять только картинки размера 25х25")
	lang_menu_link = models.CharField(
		max_length=15,
		choices=LANGUAGE_CHOICES,
		default='Ru')

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
	lang_footer_link = models.CharField(
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
