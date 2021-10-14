# Generated by Django 3.2.7 on 2021-10-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footerobject',
            options={'verbose_name': 'Объект футера', 'verbose_name_plural': 'Объекты футера'},
        ),
        migrations.AlterModelOptions(
            name='menuobject',
            options={'verbose_name': 'Объект меню', 'verbose_name_plural': 'Объекты меню'},
        ),
        migrations.AlterField(
            model_name='menuobject',
            name='icon',
            field=models.ImageField(help_text='Добавлять только картинки размера 25х25', unique=True, upload_to='media/icons_menu'),
        ),
    ]
