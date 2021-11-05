from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver

LANGUAGE_CHOICES = [
    ('Ru', 'Русский'),
    ('Kg', 'Кыргызский'),
    ('En', 'Английский'),
]

SCHOOL_SUBJECTS = [
    ('Math_ru', 'Математика(русский язык)'),
    ('Math_kg', 'Математика(кыргызский')
]


class OnlineTest(models.Model):
    name = models.CharField(max_length=50, verbose_name='Предмет')
    part_num = models.IntegerField(default=1, verbose_name='Часть')
    version = models.IntegerField(default=1, verbose_name='Вариант')
    duration = models.IntegerField(verbose_name='Время (в минутах)')
    num_questions = models.IntegerField(verbose_name='Количество вопросов')
    num_answers = models.IntegerField(verbose_name='Количество вариантов ответа')
    language = models.CharField(max_length=15, default='Ru', choices=LANGUAGE_CHOICES, verbose_name='Язык теста')
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

    class Meta:
        verbose_name = 'вопрос к тесту'
        verbose_name_plural = 'Вопросы к тесту'


CORRECT_ANS_CHOICES = [
    ('А', 'А'),
    ('Б', 'Б'),
    ('В', 'В'),
    ('Г', 'Г'),
    ('Д', 'Д'),
    ('Е', 'Е'),
]


class AnswerTest(models.Model):
    onlinetest = models.ForeignKey(OnlineTest, on_delete=models.CASCADE, related_name='answers')
    question_number = models.IntegerField(verbose_name='Номер вопроса', blank=True)
    correct_answer = models.CharField(default='А', choices=CORRECT_ANS_CHOICES, verbose_name='Правильный ответ',
                                      max_length=2, blank=True)

    class Meta:
        verbose_name = 'Ответ к тесту'
        verbose_name_plural = 'Ответы к тесту'

    def __str__(self):
        return self.onlinetest.name
