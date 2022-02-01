# Generated by Django 3.2 on 2021-12-02 20:14

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
            ],
            options={
                'verbose_name': 'Вопросы и ответы',
                'verbose_name_plural': 'Вопросы и ответы',
            },
        ),
    ]
