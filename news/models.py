from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    LANGUAGE = [
        ('ru', 'Русский'),
        ('kg', 'Кыргызский'),
    ]

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, help_text='Выберите язык')
    text = RichTextUploadingField(verbose_name='Текст')
    important = models.BooleanField(default=False, verbose_name='Важная новость')
    language = models.CharField(max_length=15, choices=LANGUAGE, verbose_name='Язык')
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE, verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.important:
            important_news = News.objects.filter(important=True)
            for news in important_news:
                news.important = False
                news.save()
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
