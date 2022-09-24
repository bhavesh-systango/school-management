
from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from requests import request
from authentication.models import CustomUser
from payment.models import Payment


class PayrollForm(forms.ModelForm):

    user = forms.ModelChoiceField(label = "User", queryset = CustomUser.objects.filter(user_type = 1), widget = forms.Select())
    amount = forms.ModelChoiceField(label = "amount", queryset = Payment.objects.all(), widget = forms.Select())
    # month_date = forms.DateField(widget = forms.DateInput(attrs = { "type": "date"}))

    class Meta:

        model = Payment
        fields = ['amount','user']


class TeacherName(forms.Form):
    
    user = forms.ModelChoiceField(label = "Teacher", queryset = CustomUser.objects.filter(user_type = 2), widget = forms.Select())

    class Meta:
        
        model = CustomUser
        field = ['user']


class StudentAmount(forms.Form):

    SECTION_AMOUNT = [

        (3000,3000),
        (4000,4000),
        (5000,5000),
        (6000,6000),
        (6000,6000),
        (7000,7000),
        (8000,8000)

        ]
    amount = forms.ChoiceField(label = "amount", choices = SECTION_AMOUNT,  widget = forms.Select())

    class Meta:

        model  = Payment
        field = ['amount']


class StudentName(forms.ModelForm):
    
    user = forms.ModelChoiceField(label = "Student", queryset = CustomUser.objects.filter(user_type = 1), widget = forms.Select())
    
    class Meta:

        model = CustomUser
        fields = ['user']


class StudentAmountName(forms.Form):

    def post(self):

        form1 = StudentName(request.POST)
        form2 = StudentAmount (request.POST)

        form1.is_valid() and form2.is_valid()
        
        form1.save()
        form2.save()