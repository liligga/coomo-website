from django.db import models
from ckeditor.fields import RichTextField


LANGUAGE_CHOICES = [
	('Ru', 'Русский'),
	('Kg', 'Кыргызский'),
	('En', 'Английский'),
]


SCHOOL_SUBJECTS = [
	('Math_ru', 'Математика'),
	('Analogies_ru', 'Аналогии и дополнения предложений'),
	('Reading_ru', 'Чтение и понимание'),
	('Grammatic_practice_ru', 'Практическая грамматика русского языка'),
	('Grammatic_practice_kg', 'Практическая грамматика кыргызского языка'),
	('History_ru', 'История'),
	('Physics_ru', 'Физика'),
	('Biology_ru', 'Биология'),
	('Chemistry_ru', 'Химия'),
	('Math_subj_ru', 'Математика предметная'),
]


class OnlineTest(models.Model):
	name = models.CharField(
		max_length=50,
		choices=SCHOOL_SUBJECTS,
		verbose_name='Предмет')
	part_num = models.IntegerField(default=1, verbose_name='Часть')
	version = models.IntegerField(default=1, verbose_name='Вариант')
	duration = models.IntegerField(verbose_name='Время (в минутах)')
	num_questions = models.IntegerField(verbose_name='Количество вопросов')
	num_answers = models.IntegerField(verbose_name='Количество вариантов ответа')
	language = models.CharField(
		max_length=15,
		default='Ru',
		choices=LANGUAGE_CHOICES,
		verbose_name='Язык теста')
	is_active = models.BooleanField(default=True, verbose_name='Опубликован')
	intro = RichTextField(verbose_name='Приветственный текст')

	class Meta:
		verbose_name = 'Онлайн тест'
		verbose_name_plural = 'Онлайн тесты'

	def __str__(self):
		return self.name


class OnlineTestQuestion(models.Model):
	onlinetest = models.ForeignKey(
		OnlineTest,
		on_delete=models.CASCADE,
		related_name='questions')
	question = models.ImageField(
		upload_to='ort/images/question/',
		verbose_name='Картинка с вопросами')
	num_start = models.IntegerField(
		verbose_name='С какого вопроса начинается тест на картинке(номер)')
	num_end = models.IntegerField(
		verbose_name='На каком вопросе заканчивается тест на картинке(номер)')

	class Meta:
		verbose_name = 'вопрос к тесту'
		verbose_name_plural = 'Вопросы к тесту'


CORRECT_ANS_CHOICES = [
	(1, 'А'),
	(2, 'Б'),
	(3, 'В'),
	(4, 'Г'),
	(5, 'Д'),
	(6, 'Е'),
]


class AnswerTest(models.Model):
	onlinetest = models.ForeignKey(
		OnlineTest,
		on_delete=models.CASCADE,
		related_name='answers')
	question_number = models.IntegerField(verbose_name='Номер вопроса')
	correct_answer = models.IntegerField(
		default=1,
		choices=CORRECT_ANS_CHOICES,
		verbose_name='Правильный ответ')

	class Meta:
		verbose_name = 'Ответ к тесту'
		verbose_name_plural = 'Ответы к тесту'
