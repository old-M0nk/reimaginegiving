from django import forms


class DonateForm(forms.Form):
    donation = forms.IntegerField(required=True)


class PaymentDetailsForm(forms.Form):
    first_name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()

