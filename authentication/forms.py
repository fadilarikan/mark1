from django import forms

from authentication.models import User


class LoginForm(forms.Form):

    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User

        fields = ('name','password')
