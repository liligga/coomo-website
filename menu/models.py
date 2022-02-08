from django.db import models

from pages.models import Page

LANGUAGE_CHOICES = [
    ('Ru', 'Русский'),
    ('Kg', 'Кыргызский'),
]
POSITION_CHOICES = [
    ('left', 'Левое меню'),
    ('bottom', 'Нижнее меню'),
    ('banner', 'На баннере'),
    ('about', 'В разделе О ЦООМО')
]

ICON_CHOICES = [
    ('<i class="fas fa-bookmark"></i>', 'ОРТ'),
    ('<i class="fas fa-copy"></i>', 'Школьная Олимпиада'),
    ('<i class="fas fa-graduation-cap"></i>', 'Абитуриентам'),
    ('<i class="fas fa-chalkboard-teacher"></i>', 'Учителям'),
]


class ActiveLinksManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class MenuLink(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    is_active = models.BooleanField(default=False, verbose_name='Активно')
    # icon = FAIconField(blank=True, null=True, verbose_name='Иконка')
    icon = models.CharField(choices=ICON_CHOICES, max_length=50, verbose_name='Иконка', blank=True, null=True)
    lang = models.CharField(
        max_length=15,
        choices=LANGUAGE_CHOICES,
        default='Ru',
        verbose_name='Язык',
        blank=True,
        null=True)
    page = models.ForeignKey(
        Page,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='Укажите страницу, если ссылка должна указывать на неё',
        verbose_name='Связанная страница',
        related_name='page_link')
    link = models.CharField(max_length=300, verbose_name='Ссылка на другие сайты или страницы этого сайта', blank=True,
                            null=True,
                            help_text='Выберите что-то одно, либо связанную страницу, либо ссылку в это поле')
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, default='left', verbose_name='Позиция меню',
                                blank=True, null=True,
                                help_text='Укажите в каком меню появится эта ссылка. В левом боковом, на баннере или ' \
                                          'нижнем среднем')
    objects = models.Manager()
    active_objects = ActiveLinksManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылка в меню'
        verbose_name_plural = 'Ссылки меню'


class FooterLink(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    link = models.URLField(max_length=200)
    lang = models.CharField(
        max_length=15,
        choices=LANGUAGE_CHOICES,
        default='Ru')

    objects = models.Manager()
    active_objects = ActiveLinksManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылка футера'
        verbose_name_plural = 'Ссылки футера'
