from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from .models import UserCustom
from aluno.models import Student


class UserForm(UserCreationForm):

    class Meta:
        model = UserCustom
        fields = ('registration', 'password1', 'password2')

    def clean_registration(self):
        registration = self.cleaned_data.get('registration')
        if not Student.objects.filter(registration=registration).exists():
            raise forms.ValidationError('Número de matrícula não existe')
        if UserCustom.objects.filter(registration=registration).exists():
            raise forms.ValidationError('Matrícula já está sendo usada!')
        return registration
