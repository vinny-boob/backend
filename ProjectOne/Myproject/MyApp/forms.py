from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import student


class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields = ['firstname','secondname','email','age','regno']
class customUser(UserCreationForm):
        class Meta:
            model=User
            fields=['username','password1','password2']