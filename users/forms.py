from django import forms


# class Email(forms.ModelForm):
#
#     class Meta:
#         model = Email
#         fields = ('email',)

class email_form(forms.Form):
    email = forms.EmailField(required=True)


class contact_us_form(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True)
    message = forms.TextInput()
