from django import forms
from .models import Email


# class Email(forms.ModelForm):
#
#     class Meta:
#         model = Email
#         fields = ('email',)

class Email(forms.Form):
    email = forms.EmailField(required=True)
    model = Email()

    def clean_message(self):
        email = self.cleaned_data.get("email")
        if Email.objects.filter(email=email).exists():
            raise forms.ValidationError("You have already registered with us")
