# Generated by Django 3.2 on 2021-12-15 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0003_auto_20211210_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinetest',
            name='name',
            field=models.CharField(choices=[('На русском', (('Math_ru', 'Математика'), ('Analogies_ru', 'Аналогии и дополнения предложений'), ('Reading_ru', 'Чтение и понимание'), ('Grammatic_practice_ru', 'Практическая грамматика русского языка'), ('History_ru', 'История'), ('Physics_ru', 'Физика'), ('Biology_ru', 'Биология'), ('Chemistry_ru', 'Химия'), ('Math_subj_ru', 'Математика предметная'), ('English_ru', 'Английский язык'))), ('Кыргызча', (('Math_kg', 'Математика'), ('Analogies_kg', 'Окшоштуктар жана сүйлөмдөрдү толуктоо'), ('Reading_kg', 'Текстти окуу жана түшүнүү'), ('Grammatic_practice_kg', 'Кыргыз тилинин практикалык грамматикасы'), ('History_kg', 'Тарых'), ('Physics_kg', 'Физика'), ('Biology_kg', 'Биология'), ('Chemistry_kg', 'Химия'), ('Math_subj_kg', 'Математика предметная'), ('English_kg', 'Англис тили')))], db_index=True, max_length=100, verbose_name='Предмет'),
        ),
    ]
