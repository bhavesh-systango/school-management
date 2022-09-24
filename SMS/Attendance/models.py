from distutils.archive_util import make_zipfile
from django.db import models
from authentication.models import CustomUser
import datetime
# Create your models here.

class Attendance(models.Model):

    choice = [

        (1,"IN"),
        (2,"OUT")
    ]

    STATUS = [
        
        (1,"Present"),
        (2,"Absent"),
    ]

    daily_attendance = models.IntegerField(choices = STATUS, default = 2) 
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    type = models.IntegerField(choices = choice, default = 1)
    time = models.DateTimeField(null = False, default = datetime.datetime.now())
    attendance_date = models.DateField(null = False, default = datetime.datetime.now())
    
    
    def __str__(self):
        
        return self.user.username + "--" + str(self.time)

  