from django import forms


class DonateForm(forms.Form):
    donation = forms.IntegerField(required=True)
