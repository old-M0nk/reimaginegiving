from django import forms


# class Email(forms.ModelForm):
#
#     class Meta:
#         model = Email
#         fields = ('email',)

class email_form(forms.Form):
    email = forms.EmailField(required=True)

    # def clean_message(self):
    #     email = self.cleaned_data.get("email")
    #     if Email.objects.filter(email=email).exists():
    #         raise forms.ValidationError("You have already registered with us")
