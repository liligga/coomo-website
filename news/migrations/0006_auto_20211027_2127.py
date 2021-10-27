# Generated by Django 3.2 on 2021-10-27 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20211026_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text='Заполняется автоматически', upload_to='news', verbose_name='Баннер новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='cover',
            field=models.ImageField(upload_to='news', verbose_name='Обложка новости'),
        ),
    ]
