from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from pytils.translit import slugify


class Page(models.Model):
    """
    Модель страниц для главной
    """
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    slug = models.SlugField(max_length=500, blank=True, null=True, unique=True)
    article = RichTextUploadingField(verbose_name='Статья')

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
