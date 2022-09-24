import datetime 
from time import time
from django.shortcuts import render,redirect
from django.views.generic.list import ListView 
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView,CreateView
from requests import request
from Attendance.forms import UpdateForm
from .models import Attendance,CustomUser
from authentication.models import CustomUser,Profile
from django.contrib.auth.mixins import LoginRequiredMixin


class UserList(LoginRequiredMixin,TemplateView):

    login_url = '/authentication/login/'
    model = CustomUser
    queryset = CustomUser.objects.all()
    context_object_name = "object_list"
    template_name = "Attendance/view_user.html"


class UserUpdateView(LoginRequiredMixin,UpdateView):

    login_url = '/authentication/login/'
    form_class = UpdateForm
    template_name = "Attendance/update_profile.html"
    success_url = '/attendance/dashboard/'
    
    queryset = CustomUser.objects.all()
    context_object_name = "user"
    

class Dashboard(LoginRequiredMixin,CreateView):

    login_url = '/authentication/login/'
    model = Attendance
    template_name = "Attendance/dashboard.html"
    fields = "__all__"


class AttendanceView(LoginRequiredMixin,TemplateView):

    login_url = '/authentication/login/'
    template_name = "Attendance/attendance.html"
    next_page = '/attendance/dashboard'
    queryset = Attendance.objects.all()
    
    def get(self, request):
     
        last_in = Attendance.objects.filter(attendance_date = datetime.datetime.now()).last() 
        if last_in == None :
            
            print(last_in)
            return render(request,"Attendance/attendance.html",{"attendance_status": 2})
            
        else  :

            print("ytgftydrtfsxetsxedtg")
            return render(request,"Attendance/attendance.html",{"attendance_status": last_in.type})


    def post(self, request ):

        print(self.get_context_data())
        print("attendance both method works")

        today_attendance = Attendance.objects.filter(attendance_date = datetime.datetime.now())   
        
        lastest_attendance = today_attendance.last()
        
        # If today attendance is registered in database then it should check what was his last status  
        if lastest_attendance != None:

            # print(lastest_attendance)
            print(today_attendance.last().type)

            # If user last tapped_in button is login then it should display log_out status
            if lastest_attendance.type == 1:

                last_swipe = today_attendance.filter(type = 1).order_by('time').last()
                first_swipe = today_attendance.first()

                first_time_swipe_data = datetime.timedelta(hours = first_swipe.time.hour,minutes = first_swipe.time.minute,seconds = first_swipe.time.second)
                last_time_swipe_data = datetime.timedelta(hours = last_swipe.time.hour,minutes = last_swipe.time.minute,seconds = last_swipe.time.second)
                
                print("********************")
                print(last_swipe)
                print(first_time_swipe_data)
                print(last_time_swipe_data)
                print(last_time_swipe_data -first_time_swipe_data )
                print("when user is logged in")
                current_attendance = Attendance.objects.create(user =request.user , type = 2, time = datetime.datetime.now() )
                print(current_attendance)

                # if (last_time_swipe_data - first_time_swipe_data) >= datetime.timedelta(hours = 9):

                #     if Attendance.objects.get( attendance_date = datetime.datetime.now()).exists:

                #         Attendance.objects.save(user = request.user, daily_attendance = 1)
                # else:

                #     Attendance.objects.create( user = request.user, daily_attendance = 2)


            #if the user last tapped_in button is logout then it should display log_in status    
            elif lastest_attendance.type == 2 :

                first_swipe = today_attendance.first()
                last_swipe =today_attendance.last()

                first_time_swipe_data = datetime.timedelta(hours = first_swipe.time.hour,minutes = first_swipe.time.minute,seconds = first_swipe.time.second)
                last_time_swipe_data = datetime.timedelta(hours = last_swipe.time.hour,minutes = last_swipe.time.minute,seconds = last_swipe.time.second)

                print("#################")
                print((datetime.timedelta(hours = 9)))
                print(first_time_swipe_data)
                print(last_time_swipe_data)
                print(last_time_swipe_data -first_time_swipe_data )
                print("when user is logged out")
                 
                if (last_time_swipe_data - first_time_swipe_data) >= datetime.timedelta(hours = 9):

                    current_attendance = Attendance.objects.create(user = request.user , type = 1,time = datetime.datetime.now(),daily_attendance = 1 )

                    # update_daily_attendance = Attendance(user = request.user)
                    # update_daily_attendance.daily_attendance = 1
                    # update_daily_attendance.save()

                else:
                    
                    current_attendance = Attendance.objects.create(user = request.user , type = 1,time = datetime.datetime.now(),daily_attendance = 2 )
                    # update_daily_attendance = Attendance(user = request.user)
                    # update_daily_attendance.daily_attendance = 2
                    # update_daily_attendance.save()

            else :

                return

        else :
            
            #if today attendance is not registered yet then it should display log_in status
            print("when object is null")
            Attendance.objects.create(user = request.user , type = 1 )
            
        return redirect('/attendance/attendancelist')

