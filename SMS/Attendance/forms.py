
from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomUser,Organization


class UpdateForm(forms.ModelForm):
 
    CHOICES = [
        (1,"student"),
        (2,"teacher"),
        (3,"admin")
    ]

    username=forms.CharField(label="Enter username",max_length=40)
    # first_name=forms.CharField(label="First name",max_length=40)
    # last_name=forms.CharField(label="Last name",max_length=40)
    email=forms.EmailField(label="Email",widget=forms.EmailInput)
    # password1=forms.CharField(label="password",widget=forms.PasswordInput)
    # password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    mobile=forms.CharField(max_length=10,widget=forms.NumberInput)
    address=forms.CharField(max_length=50)
    user_type=forms.ChoiceField(choices = CustomUser.CHOICES)
    # organization_name = forms.CharField(max_length=40)
    organization_name = forms.ModelChoiceField(queryset=Organization.objects.all(), widget=forms.Select())

    class Meta:
        
        model = CustomUser
        fields = ["first_name","last_name","organization_name","mobile","email","address","username"]
