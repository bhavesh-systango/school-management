
from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from payment.models import Payment


class PaymentForm(forms.ModelForm):
    
    amount = forms.IntegerField()
    # type = forms.ChoiceField(choices = Payment.DB)

    # trasaction_date = forms.DateField(widget=forms.DateInput)
    
    class Meta:

        model = Payment
        fields = ['amount']

