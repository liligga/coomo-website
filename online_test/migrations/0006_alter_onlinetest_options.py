# Generated by Django 3.2 on 2024-11-11 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0005_auto_20241112_0443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onlinetest',
            options={'ordering': ['order_number'], 'verbose_name': 'Онлайн тест', 'verbose_name_plural': 'Онлайн тесты'},
        ),
    ]