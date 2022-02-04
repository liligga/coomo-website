import re
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
from io import BytesIO
from django.core.files import File
from pytils.translit import slugify
from django.template.defaultfilters import truncatewords
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CLEAN_RE = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


def clean_html(raw_html):
    clean_text = re.sub(CLEAN_RE, '', raw_html)
    return clean_text


class News(models.Model):
    LANGUAGE = [
        (None, 'Выберите язык'),
        ('Ru', 'Русский'),
        ('Kg', 'Кыргызский'),
    ]

    title = models.CharField(max_length=500, verbose_name='Заголовок')
    slug = models.SlugField(max_length=500, blank=True, null=True, unique=True)
    article = RichTextUploadingField(verbose_name='Статья')
    excerpt = models.TextField(blank=True, null=True, verbose_name='Отрывок из статьи')
    important = models.BooleanField(default=False, verbose_name='Важное')
    lang = models.CharField(
        max_length=15,
        choices=LANGUAGE,
        verbose_name='Язык',
        default='Ru')
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE, verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    cover = models.ImageField(
        upload_to='news',
        blank=True,
        verbose_name='Обложка')
    banners = models.BooleanField(default=False, verbose_name='Баннер')
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительская новость',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='news')
    project = models.BooleanField(default=False, verbose_name='Проект', help_text='Эта запись является Проектом')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + str(self.id)
        clean_text = clean_html(self.article)
        self.excerpt = truncatewords(clean_text, 30)
        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']

    def make_thumbnail(self, cover, size=(200, 350)):
        img = Image.open(cover)
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=cover.name)
        return thumbnail

# def news_pre_save(sender, instance, *args, **kwargs):
#     if instance.important:
#         try:
#             important_news = News.objects.get(important=True)
#             if instance != important_news:
#                 important_news.important = False
#                 important_news.save()
#         except News.DoesNotExist:
#             pass


# @receiver(post_save, sender=News)
# def news_save(sender, instance, created, **kwargs):
#     if created:
#         if not instance.parent:
#             instance.parent = instance
#             instance.save()


# pre_save.connect(news_pre_save, sender=News)
