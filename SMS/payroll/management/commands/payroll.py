from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMessage
from requests import request
from SMS.Attendance.models import Attendance
from payment.models import Payment
from authentication.models import CustomUser
import datetime


class Command(BaseCommand):

    help = "It is used to distribute payroll to teachers"

    def handle(self, *args, **options, ):

        try:
  
            today = datetime.datetime.now()
            month =  today.month
            filter_payment = Payment.objects.filter(type = 1, status = 2, paid_date__month = month )
            print("****************8")
            print(filter_payment)

            if filter_payment.exists() :

                user1 = CustomUser.objects.filter(user_type = 1)
                attendance = Attendance.objects.filter(daily_attendance = 1 )

                for user in user1:

                    print(user.pk)
                    print("###########")
                    create_payroll = Payment.objects.create(user = CustomUser(user.pk), type = 1, amount = 8000, status = 2, paid_date = datetime.datetime.now())
                    # create_form_payroll = Payment.objects.create(type = 2, amount = 10000, status = 2, paid_date = datetime.datetime.now())
                    print(create_payroll)


        except Exception as e:

            raise CommandError(e)