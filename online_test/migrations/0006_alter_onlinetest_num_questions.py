# Generated by Django 3.2.7 on 2021-10-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0005_answertest_onlinetestquestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinetest',
            name='num_questions',
            field=models.IntegerField(verbose_name='Количество вопросов'),
        ),
    ]
