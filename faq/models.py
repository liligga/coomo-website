from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=500, unique=True, verbose_name='Вопрос')
    answer = models.CharField(max_length=1500, verbose_name='Ответ на вопрос')

    def __str__(self):
        return f'{self.question}'

    class Meta:
        verbose_name = 'Вопросы и ответы'
        verbose_name_plural = 'Вопросы и ответы'
