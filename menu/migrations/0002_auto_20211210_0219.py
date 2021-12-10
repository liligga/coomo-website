# Generated by Django 3.2 on 2021-12-09 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulink',
            name='link',
            field=models.CharField(blank=True, help_text='Выберите что-то одно, либо связанную страницу, либо ссылку в это поле', max_length=300, null=True, verbose_name='Ссылка на другие сайты или страницы этого сайта'),
        ),
        migrations.AlterField(
            model_name='menulink',
            name='position',
            field=models.CharField(blank=True, choices=[('left', 'Левое меню'), ('bottom', 'Нижнее меню'), ('banner', 'На баннере')], default='left', help_text='Укажите в каком меню появится эта ссылка. В левом боковом, на баннере или нижнем среднем', max_length=10, null=True, verbose_name='Позиция меню'),
        ),
    ]
