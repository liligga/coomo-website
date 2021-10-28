import re
from django.db import models
from django.contrib.auth.models import User
# from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from PIL import Image
from pytils.translit import slugify
from django.template.defaultfilters import truncatewords

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

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(blank=True, null=True, unique=True)
    article = RichTextUploadingField(verbose_name='Статья')
    excerpt = models.TextField(blank=True, null=True, verbose_name='Отрывок из статьи')
    important = models.BooleanField(default=False, verbose_name='Важное')
    language = models.CharField(max_length=15, choices=LANGUAGE, verbose_name='Язык', default='Ru')
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE, verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    cover = models.ImageField(upload_to='uploads', blank=True, verbose_name='Обложка')
    banners = models.BooleanField(default=False, verbose_name='Баннер')
    parent = models.ForeignKey('self', verbose_name='Родительская новость', on_delete=models.SET_NULL, blank=True,
                               null=True, related_name='news', )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        clean_text = clean_html(self.article)
        self.excerpt = truncatewords(clean_text, 35)
        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


def news_pre_save(sender, instance, *args, **kwargs):
    if instance.important:
        try:
            important_news = News.objects.get(important=True)
            if instance != important_news:
                important_news.important = False
                important_news.save()
        except News.DoesNotExist:
            pass


@receiver(post_save, sender=News)
def news_save(sender, instance, created, **kwargs):
    if created:
        if not instance.parent:
            instance.parent = instance
            instance.save()


pre_save.connect(news_pre_save, sender=News)
