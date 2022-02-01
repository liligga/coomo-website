from django import forms
from django.core.exceptions import ValidationError

from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

    def clean(self):
        news = News.objects.filter(banners=True).exists()

        if not news:
            raise ValidationError({'banners': 'Нужна хотя бы одна новость в баннере. Отметьте галочку'})
