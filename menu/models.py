from django.db import models


LANGUAGE_CHOICES = [
	('Ru', 'Русский'),
	('Kg', 'Кыргызский'),
	('En', 'Английский'),
 ]
class ActiveObjectsManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

class MenuObject(models.Model):
	title = models.CharField(max_length=100)
	is_active = models.BooleanField(default=False)
	link = models.URLField(max_length=200)
	icon = models.ImageField(upload_to='media/icons_menu', unique=True, help_text="Добавлять только картинки размера 25х25")
	lang_menu_object = models.CharField(max_length=15, choices=LANGUAGE_CHOICES, default='Ru')

	objects = models.Manager()
	active_objects = ActiveObjectsManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Объект меню'
		verbose_name_plural='Объекты меню'

class FooterObject(models.Model):
	title = models.CharField(max_length=100)
	is_active = models.BooleanField(default=False)
	link = models.URLField(max_length=200)
	lang_footer_object = models.CharField(max_length=15, choices=LANGUAGE_CHOICES, default='Ru')

	objects = models.Manager()
	active_objects = ActiveObjectsManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Объект футера'
		verbose_name_plural='Объекты футера'