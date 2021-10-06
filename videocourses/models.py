from django.db import models


LANGUAGE_CHOICES = [
	('Ru', 'Русский'),
	('Kg', 'Кыргызский'), #Слово "Кыргызский" можно поменять на "Кыргызча" по желанию
	('En', 'Английский'), #Слово "Английский" можно поменять на "English" по желанию
 ]

class EngCoursesManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(lang_course='En')

class KgCoursesManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(lang_course='Kg')


class Course(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(unique=True)
	lang_course = models.CharField(default="Ru", choices=LANGUAGE_CHOICES, max_length=15)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Курс'
		verbose_name_plural='Курсы'

	objects = models.Manager()
	eng_objects = EngCoursesManager()
	kg_objects = KgCoursesManager()


class Video(models.Model):
	course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name='videos')
	name = models.CharField(max_length=150)
	video_link = models.URLField(max_length = 150, unique=True, blank=True)
	lang_video = models.CharField(default='Ru', choices=LANGUAGE_CHOICES, max_length=15)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Видео'
		verbose_name_plural='Видео'
