import datetime
from django.db import models
from authentication.models import CustomUser
from Attendance.models import Attendance    

# Create your models here.
# class AmountChoices(models.IntegerChoices):

#     grade1 =[('1','3000'),
#             ('2','4000'),
#             ('3','5000'),
#             ('4','6000'),
#             ('5','6000'),
#             ('6','7000'),
#             ('7','8000')]


class Payment(models.Model):

    DB = [

        (1,"Credit"),
        (2,"Debit") 
    ]

    PAY_STATUS = [

        (1,"paid"),
        (2,"unpaid")
    ]

    SECTION_AMOUNT = [

        (3000,3000),
        (4000,4000),
        (5000,5000),
        (6000,6000),
        (6000,6000),
        (7000,7000),
        (8000,8000)
    ]

    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    amount = models.IntegerField(choices = SECTION_AMOUNT)
    # teacher_student_amount = models.IntegerField(default = AmountChoices.LOW, choices = AmountChoices.choices) 
    # attendance = models.ForeignKey(Attendance,on_delete = models.CASCADE)
    type = models.IntegerField(choices = DB)
    paid_date = models.DateTimeField(default = datetime.datetime.now())
    status = models.IntegerField(choices = PAY_STATUS, default = 2 )

    def __str__(self):

        return self.user.username + "--" + str(self.amount)