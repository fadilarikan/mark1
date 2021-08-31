from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from authentication.models import LoginUser


class LoginForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = LoginUser

        fields = ('name', 'password')


class NewUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kullanıcı Adı",
                "class": "form-control form-control-lg border-0"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email Adresiniz",
                "class": "form-control form-control-lg border-0"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Şifre",
                "class": "form-control form-control-lg border-0"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Şifre Tekrarı",
                "class": "form-control form-control-lg border-0"
            }
        ))

    class Meta:
        model = User

        fields = ('username', 'email', 'password1', 'password2')
