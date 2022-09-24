import datetime

from Attendance.forms import UpdateForm
from authentication.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
# Create your views here.
from payment.models import Payment

from .form import PayrollForm, StudentAmountName


class ShowPayroll(LoginRequiredMixin, TemplateView):

    login_url = "/authentication/login/"
    template_name = "payroll/show_payment.html"

    def get(self, request):

        teacher_payroll_amount = Payment.objects.filter(user = request.user,status = 1).values_list('amount')

        return render(request,"payroll/show_payment.html", {"payment" : teacher_payroll_amount} )
        

class Payroll(LoginRequiredMixin, CreateView):
    
    login_url = "/authentication/login/"
    template_name = "payroll/teacher_payroll.html"
    form_class = PayrollForm
    # success_url = '/attendance/dashboard/'
    queryset = Payment.objects.all()
    context_object_name = "teacher_payroll"
    user = CustomUser.objects.all()

    extra_context = {

        "user" : user,
        "payment" : queryset
    }

    def post(self, request):

        pay_to_user = request.POST["user"];
        print(pay_to_user)
  
        today = datetime.datetime.now()
        month =  today.month
        filter_payment = Payment.objects.select_related('user').filter(user = pay_to_user , user__user_type = 2, type = 2, status = 2, paid_date__month = month )
        print(filter_payment)

        for user in filter_payment: 

            print("****************8")
            print(user)

            if not filter_payment.exists():

                print("###########")
                #  Payment.objects.values_list('amount').filter(user = request.user) 
                # create_payroll = Payment.objects.value_list('amount').create( type = 2, user = CustomUser(pay_to_user), paid_date = datetime.datetime.now(), status = 1 )
                filter_payment.type = 2
                filter_payment.paid_date = datetime.datetime.now()
                filter_payment.status = 1
                filter_payment.amount = Payment.objects.values_list('amount').filter(user = request.user)
                filter_payment.save()
                print(filter_payment)

        return render(request, "Attendance/dashboard.html")

    def get(self, request):

        print("***********88888")
        name = CustomUser.objects.filter(user = request.user).first().username
        filter_teacher = Payment.objects.select_related('user').filter( status = 1,user__user_name = name)
            
        return render( request, "payroll/teacher_payroll.html",{ "filter_teacher" : filter_teacher} )


class StudentPage(LoginRequiredMixin, UpdateView):
    
    login_url = '/authentication/login/'
    form_class = StudentAmountName
    template_name = "Attendance/teacher_form.html"
    success_url = '/attendance/dashboard/'

    def post(self, request):

        filter_user = Payment.objects.select_related('user').filter(user = request.user, )
