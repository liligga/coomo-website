from django import forms
from django.core.exceptions import ValidationError

from menu.models import MenuLink


class MenuLinkForm(forms.ModelForm):
    class Meta:
        model = MenuLink
        fields = '__all__'

    def clean(self):
        position = self.cleaned_data.get('position')
        icon = self.cleaned_data.get('icon')
        link = self.cleaned_data.get('link')
        page = self.cleaned_data.get('page')
        if position == 'banner' and link is None:
            raise ValidationError({'link': 'Введите ссылку!'})
        elif position != 'banner' and page is None:
            raise ValidationError({'page': 'Укажите страницу!'})
        elif position == 'left' and icon is None:
            raise ValidationError({'icon': 'Укажите иконку!'})
