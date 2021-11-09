from django import forms

from online_test.models import OnlineTest


class ExcelForm(forms.Form):
    excel_file = forms.FileField(label='Таблица с ответами')

    def __init__(self, *args, **kwargs):
        super(ExcelForm, self).__init__(*args, **kwargs)
        self.fields['excel_file'].required = False

