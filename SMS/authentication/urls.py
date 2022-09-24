from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "authentication"

urlpatterns = [

    path('register/',views.register,name="register"),
    path('home/',views.home,name="home"),
    # path('dashboard/',views.Dashboard.as_view(),name="dashboard"),
    path('logout/',views.UserLogout.as_view(),name="logout"),
    path('login/', views.LoginPage.as_view(),name='login'),
    path('passwordreset/',views.PasswordReset.as_view(),name = "password_reset"),
    path('passwordresetcomplete/',views.PasswordResetComplete.as_view(),name = "password_reset_complete"),
    path('passwordresetdone/',views.PasswordResetDone.as_view(),name = "password_reset_done"),
    path('passwordchange/',views.PasswordChange.as_view(), name = "password_change"),
    path('passwordresetconfirm/',views.PasswordResetConfirm.as_view(),name = "password_reset_confirm"),
    path('passwordchangedone/',views.PasswordChangeDone.as_view(), name = "password_change_done"),
    path('admindashboard/',views.admin_dashboard, name = "admin_dashboard"),
    path('teacherdashboard/', views.teacher_dashboard, name = 'teacher_dashboard'),
    path('deleteuser/<int:user_id>',views.DeleteUser.as_view(), name = "delete_user")

    # path('update_profile/<int:pk>/',views.ProfileView.as_view(),name="update_profile")
]

