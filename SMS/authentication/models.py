
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class Organization(models.Model):

    CHOICE = [

        (1,"School"),
        (2,"University")
    ]

    organization_name = models.CharField(max_length=40)
    contact_number = models.CharField(max_length=14)
    type = models.IntegerField(choices = CHOICE,default = 1)
    email=models.EmailField(unique = True)
    address=models.CharField(max_length = 50)
    admin_name=models.CharField(max_length = 20 , default = "admin")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    def __str__(self):

        return  self.organization_name


class CustomUser(AbstractUser):

    CHOICES = [

        (1,"student"),
        (2,"teacher"),
        (3,"admin")
    ]
    
    user_type= models.IntegerField(choices = CHOICES)
    email = models.EmailField(_('email address'),unique = True)
    organization = models.ForeignKey(Organization,on_delete = models.CASCADE,null = True)
    username = models.CharField(unique = False, max_length=40)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = ["password"]

    objects = CustomUserManager()

    def __str__(self):

        return "{}".format(self.email)


class Profile(models.Model):

    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)  
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

    REQUIRED_FIELDS = ["mobile"]

    def __str__(self):
        
        return "{0} - {1}".format(self.user.first_name,self.mobile)

