# Generated by Django 3.2.7 on 2021-10-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0003_alter_onlinetest_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinetest',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Опубликован'),
        ),
    ]
