from dataclasses import fields

from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from keyring import set_password
from authentication.models import CustomUser, Organization, Profile


class RegisterForm(forms.ModelForm):
 
    CHOICES = [

        (1,"student"),
        (2,"teacher"),
        (3,"admin")
    ]

    username = forms.CharField(label = "Enter username",max_length = 40)
    # first_name=forms.CharField(label="First name",max_length=40)
    # last_name=forms.CharField(label="Last name",max_length=40)
    email = forms.EmailField(label = "Email",widget = forms.EmailInput)
    password1 = forms.CharField(label = "password",widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirm Password",widget = forms.PasswordInput)
    mobile = forms.CharField(max_length = 10,widget = forms.NumberInput)
    address = forms.CharField(max_length = 50)
    user_type = forms.ChoiceField(choices = CustomUser.CHOICES)
    # organization_name = forms.CharField(max_length=40)
    organization_name = forms.ModelChoiceField(queryset = Organization.objects.all(), widget = forms.Select())

    class Meta:
    
        model = CustomUser
        fields = ["first_name","last_name","organization_name","mobile","email","address","password1","password2"]
    
    def clean_username(self):

        username = self.cleaned_data['username'].lower()

        if CustomUser.objects.filter(username=username):

            raise  ValidationError("Username already exists")
        return username    

    def clean_email(self):

        email = self.cleaned_data['email'].lower()

        if CustomUser.objects.filter(email=email):
            raise ValidationError(" Email already exists")
        return email

    def clean_password(self):

        password1 = self.cleaned_data.get("password")        
        password2 = self.cleaned_data.get("password")        
        
        if password1 and password2 and password1 != password2 :

            raise ValidationError(" Password is same ")

        return password1  

    def save(self):

        user = CustomUser()
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.set_password(self.cleaned_data["password1"])
        user.save()
       
        userprofile = Profile.objects.create(
            user = user,
            mobile = self.cleaned_data["mobile"],
            address = self.cleaned_data["address"] 
        )
 
        return user,userprofile


class AdminSignUp(UserCreationForm) :

    organization_name = forms.CharField(max_length=40,required=True)
    contact_number = forms.CharField(max_length=14,widget=forms.NumberInput)
    type = forms.ChoiceField(required=True,choices = Organization.CHOICE)
    email=forms.EmailField(required=True,widget=forms.EmailInput)
    address=forms.CharField(max_length=50)
    admin_name=forms.CharField(max_length=20,required=True)

    class Meta : 

        model = Organization
        fields = ["organization_name","contact_number","type","email","address","admin_name","password1","password2"]

    def clean_email(self):

        email=self.cleaned_data['email'].lower()

        if Organization.objects.filter(email=email):

            raise ValidationError(" Email already exists")
        return email

    def clean_password(self):

        password1=self.cleaned_data.get("password1")        
        password2=self.cleaned_data.get("password2")        
        
        if password1 and password2 and password1 != password2 :
            
            raise ValidationError(" Password is same ")

        return password1  

    def save(self):
    
        user = Organization()
        user.organization_name = self.cleaned_data["organization_name"]
        user.email = self.cleaned_data["email"]
        user.type = self.cleaned_data["type"]
        user.address = self.cleaned_data["address"]
        user.admin_name = self.cleaned_data["admin_name"]
        user.contact_number = self.cleaned_data["contact_number"]
        user.set_password(self.cleaned_data["password1"])
        user.save()
        
        return user

