# Generated by Django 3.2 on 2021-11-09 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название галлереи')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание галлереи')),
                ('author', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Галлерея',
                'verbose_name_plural': 'Галлереи',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=gallery.models.get_upload_to, verbose_name='Картинка')),
                ('gallery_id', models.ForeignKey(help_text='Выберите к какой галлерее будет принадлежать картинки', on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='gallery.gallery', verbose_name='Имя галлереи')),
            ],
            options={
                'verbose_name': 'Картинка в галлерее',
                'verbose_name_plural': 'Картинки в галлерее',
            },
        ),
    ]
