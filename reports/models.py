from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Reports(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    pdf = models.FileField(verbose_name='Документ')
    article = RichTextUploadingField(verbose_name='Текст страницы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'