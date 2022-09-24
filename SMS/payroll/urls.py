from django.contrib import admin
from django.urls import path,include
from .views import Payroll,ShowPayroll


app_name = "payroll"

urlpatterns = [

    path('teacherpayroll/', Payroll.as_view(), name = "teacher_payroll"),
    path('showpayroll/', ShowPayroll.as_view(), name = "show_payroll"),
    # path('studentForm/', StudentPage.as_view(), name = "student_page" ),
    # path('teacherpage/',TeacherPage.as_view(), name = "teacher_page")

]

