from django.urls import path
from .views import UserList,UserUpdateView,AttendanceView,Dashboard

app_name = "Attendance"

urlpatterns = [

    path('userlist/', UserList.as_view() , name = "user_view"),
    path('updateuser/<int:pk>/',UserUpdateView.as_view(),name="user_update"),
    path('dashboard/',Dashboard.as_view(),name="dashboard"),
    path('attendancelist/',AttendanceView.as_view(),name='attendance'),
    path('userupdateview/<int:pk>/',UserUpdateView.as_view(),name="update_user")

]
