# Generated by Django 3.2 on 2022-03-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, unique=True, verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=1500, verbose_name='Ответ на вопрос')),
                ('lang', models.CharField(blank=True, choices=[('Ru', 'Русский'), ('Kg', 'Кыргызский')], default='Ru', max_length=40, null=True, verbose_name='Язык вопроса-ответа')),
            ],
            options={
                'verbose_name': 'Вопросы и ответы',
                'verbose_name_plural': 'Вопросы и ответы',
            },
        ),
    ]