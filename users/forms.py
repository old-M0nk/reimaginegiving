from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model


class email_form(forms.Form):
    email = forms.EmailField(required=True)


class contact_us_form(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True)
    message = forms.TextInput()


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    #widget=forms.PasswordInput hides the password with bullets or *


class UserRegistrationForm(forms.Form):
    username = forms.EmailField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)


