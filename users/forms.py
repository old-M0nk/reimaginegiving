from django.contrib.auth.models import User
from django import forms


class email_form(forms.Form):
    email = forms.EmailField(required=True)


class contact_us_form(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True)
    message = forms.TextInput()


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
