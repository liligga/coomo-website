# Generated by Django 3.2 on 2021-10-31 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news', to='news.news', verbose_name='Родительская новость'),
        ),
        migrations.AddField(
            model_name='news',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='news'),
        ),
        migrations.AlterField(
            model_name='news',
            name='cover',
            field=models.ImageField(blank=True, upload_to='news', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='news',
            name='language',
            field=models.CharField(choices=[(None, 'Выберите язык'), ('Ru', 'Русский'), ('Kg', 'Кыргызский')], default='Ru', max_length=15, verbose_name='Язык'),
        ),
    ]
