from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

class AddItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Basket
        exclude = ['user']
        widgets = {
            'id_tovara': forms.HiddenInput(),
            'amount_of_items': forms.HiddenInput(),
        }


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))