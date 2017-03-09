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

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     if username and password:
    #         user = authenticate(username='username', password='password')
    #         if not user:
    #             raise forms.ValidationError("This user does not exist")
    #
    #         if not user.check_password(password):
    #             raise forms.ValidationError("Incorrect Username or password")
    #
    #         if not user.is_active:
    #             raise forms.ValidationError("This user is no longer active")
    #         return super(UserLoginForm, self).clean()


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password" , widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean_password2(self):
        password= self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords don't match")
        return super(UserRegistrationForm, self).clean()
