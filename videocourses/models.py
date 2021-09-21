from django.db import models

LANGUAGE_CHOICES = [
	('Ru', 'Русский'),
	('Kg', 'Кыргызский'), #Слово "Кыргызский" можно поменять на "Кыргызча" по желанию
	('En', 'Английский'), #Слово "Английский" можно поменять на "English" по желанию
 ]

class Course(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(unique=True)
	lang_course = models.CharField(default="Ru", choices=LANGUAGE_CHOICES, max_length=15)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Курс'
		verbose_name_plural='Курсы'


class Video(models.Model):
	course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
	name = models.CharField(max_length=150)
	video_link = models.URLField(max_length = 150, unique=True, blank=True)
	lang_video = models.CharField(default='Ru', choices=LANGUAGE_CHOICES, max_length=15)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Видео'
		verbose_name_plural='Видео'