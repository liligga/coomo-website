# Generated by Django 3.2.7 on 2021-11-04 16:55

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('article', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Статья')),
                ('excerpt', models.TextField(blank=True, null=True, verbose_name='Отрывок из статьи')),
                ('important', models.BooleanField(default=False, verbose_name='Важное')),
                ('language', models.CharField(choices=[(None, 'Выберите язык'), ('Ru', 'Русский'), ('Kg', 'Кыргызский')], default='Ru', max_length=15, verbose_name='Язык')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('cover', models.ImageField(blank=True, upload_to='uploads', verbose_name='Обложка')),
                ('banners', models.BooleanField(default=False, verbose_name='Баннер')),
                ('author', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news', to='news.news', verbose_name='Родительская новость')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
