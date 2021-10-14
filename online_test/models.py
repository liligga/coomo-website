from django.db import models
from ckeditor.fields import RichTextField


LANGUAGE_CHOICES = [
	('Ru', 'Русский'),
	('Kg', 'Кыргызский'),
	('En', 'Английский'),
 ]

SCHOOL_SUBJECTS = [
	('Math_ru', 'Математика(русский язык)'),
	('Math_kg', 'Математика(кыргызский язык)')
]
class OnlineTest(models.Model):
	name = models.CharField(max_length=50, verbose_name='Предмет')
	part_num = models.IntegerField(default=1, verbose_name='Часть')
	version = models.IntegerField(default=1, verbose_name='Вариант')
	duration = models.IntegerField(verbose_name='Время (в минутах)')
	num_questions = models.IntegerField(verbose_name='Количество заданий')
	num_answers = models.IntegerField(verbose_name='Количество вариантов ответа')
	language = models.CharField(max_length=15,default='Ru', choices=LANGUAGE_CHOICES, verbose_name='Язык теста')
	is_active = models.BooleanField(default=True, verbose_name='Опубликован')
	intro = RichTextField(verbose_name='Приветственный текст')

	class Meta:
		verbose_name = 'Онлайн тест'
		verbose_name_plural = 'Онлайн тесты'


	def __str__(self):
		return self.name