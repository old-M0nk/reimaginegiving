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


class NGORegistrationForm(forms.Form):
    name = forms.CharField()
    sector = forms.CharField()
    since = forms.CharField()
    location = forms.CharField()
    legal_id = forms.CharField()
    affiliation = forms.CharField()
    board_no = forms.CharField()
    employee_no = forms.CharField()
    min_pay = forms.CharField()
    avg_pay = forms.CharField()
    offices_no = forms.CharField()
    office_loc = forms.CharField()


class NotificationForm(forms.Form):
    username = forms.IntegerField(required=True)
    supported_projects_mobile = forms.BooleanField()
    supported_projects_email = forms.BooleanField()
    general_mobile = forms.BooleanField()
    general_email = forms.BooleanField()
    exciting_projects_mobile = forms.BooleanField()
    exciting_projects_email = forms.BooleanField()


