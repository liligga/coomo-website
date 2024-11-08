# Generated by Django 3.2 on 2022-03-17 19:15

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250, verbose_name='Заголовок')),
                ('pdf', models.FileField(upload_to='', verbose_name='Документ')),
                ('article', ckeditor_uploader.fields.RichTextUploadingField(db_index=True, verbose_name='Текст страницы')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
            },
        ),
    ]
