from django.forms import ModelForm
from .models import User

class Reg_from(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'tg',
            'password'
        ]

class Log_form(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'tg',
            'password'
        ]

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get('first_name')
        tg = cleaned_data.get('tg')
        password = cleaned_data.get('password')

        