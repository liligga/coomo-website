from django import forms
from django.core.exceptions import ValidationError

from .models import News
from pdb import set_trace


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def clean(self):
        all_news = News.objects.filter(banners=True).exists()
        cleaned_data = super().clean()

        if not cleaned_data.get("banners") and not all_news:
            raise ValidationError(
                {
                    "banners": "Нужна хотя бы одна новость в баннере. Отметьте галочку"
                }
            )

        return super().clean()
