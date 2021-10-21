from django.db import models
from ckeditor.fields import RichTextField


LANGUAGE_CHOICES = [
	('Ru', 'Русский'),
	('Kg', 'Кыргызский'),
	('En', 'Английский'),
 ]

SCHOOL_SUBJECTS = [
	('Math_ru', 'Математика(русский язык)'),
	('Math_kg', 'Математика(кыргызский язык)'),
	('Analogies_ru', 'Аналогии и дополнения предложений(русский язык)'),
	('Analogies_kg', 'Аналогии и дополнения предложений(кыргызский язык)'),
	('Reading_ru', 'Чтение и понимание(русский язык)'),
	('Reading_kg', 'Чтение и понимание(кыргызский язык)'),
	('Grammatic_practice_ru', 'Практическая грамматика русского языка'),
	('Grammatic_practice_kg', 'Практическая грамматика кыргызского языка'),
	('History_ru', 'История(русский язык)'),
	('History_kg', 'История(кыргызский язык)'),
	('Physics_ru', 'Физика(русский язык)'),
	('Physics_kg', 'Физика(кыргызский язык)'),
	('Biology_ru', 'Биология(русский язык)'),
	('Biology_kg', 'Биология(кыргызский язык)'),
	('Chemistry_ru', 'Химия(русский язык)'),
	('Chemistry_kg', 'Химия(кыргызский язык)'),
	('Math_subj_ru', 'Математика предметная(русский язык)'),
	('Math_subj_kg', 'Математика предметная(кыргызский язык)')
]
class OnlineTest(models.Model):
	name = models.CharField(max_length=50, verbose_name='Предмет')
	part_num = models.IntegerField(default=1, verbose_name='Часть')
	version = models.IntegerField(default=1, verbose_name='Вариант')
	duration = models.IntegerField(verbose_name='Время (в минутах)')
	num_questions = models.IntegerField(verbose_name='Количество вопросов')
	num_answers = models.IntegerField(verbose_name='Количество вариантов ответа')
	language = models.CharField(max_length=15,default='Ru', choices=LANGUAGE_CHOICES, verbose_name='Язык теста')
	is_active = models.BooleanField(default=True, verbose_name='Опубликован')
	intro = RichTextField(verbose_name='Приветственный текст')

	class Meta:
		verbose_name = 'Онлайн тест'
		verbose_name_plural = 'Онлайн тесты'


	def __str__(self):
		return self.name


class OnlineTestQuestion(models.Model):
	onlinetest = models.ForeignKey(OnlineTest, on_delete=models.CASCADE, related_name='questions')
	question = models.ImageField(upload_to='ort/images/question/', verbose_name='Картинка с вопросами')
	num_start = models.IntegerField(verbose_name='С какого вопроса начинается тест на картинке(номер)')
	num_end = models.IntegerField(verbose_name='На каком вопросе заканчивается тест на картинке(номер)')


CORRECT_ANS_CHOICES = [
	(1, 'А'),
	(2, 'Б'),
	(3, 'В'),
	(4, 'Г'),
	(5, 'Д'),
	(6, 'Е'),
]


class AnswerTest(models.Model):
	onlinetest = models.ForeignKey(OnlineTest, on_delete=models.CASCADE, related_name='answers')
	question_number = models.IntegerField(verbose_name='Номер вопроса')
	correct_answer = models.IntegerField(default=1, choices=CORRECT_ANS_CHOICES, verbose_name='Правильный ответ')
