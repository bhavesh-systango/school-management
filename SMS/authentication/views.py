import email
import pdb
from django.shortcuts import redirect, render
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as auth_login
from requests import request
from authentication.models import CustomUser
from .forms import RegisterForm 
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView,LogoutView, PasswordResetCompleteView,PasswordResetView,PasswordChangeView,PasswordResetConfirmView, PasswordChangeDoneView, PasswordResetDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView , UpdateView ,DetailView,TemplateView, DeleteView
from django.contrib.auth.decorators import login_required


# class ProfileView(UpdateView,LoginRequiredMixin) :
#     model= CustomUser
#     form_class = AdminSignUp
#     success_url = reverse_lazy('home')
#     template_name = 'registration/update_profile.html'


# class SignUpView(CreateView) :
#     template_name = "registration/admin_register.html"  
#     success_url = reverse_lazy('login')
#     form_class = AdminSignUp  

class LoginPage(LoginView):

    template_name="registration/login.html"

    def form_valid(self, form):

        """Security check complete. Log the user in."""

        auth_login(self.request, form.get_user())
        print(self.request.user)
        user = CustomUser.objects.filter(email = self.request.user).first()
        print(user)
        print(user.user_type)

        if user.user_type == 1:

            return redirect("/attendance/dashboard")

        elif user.user_type == 2:

            return redirect("/attendance/teacherdashboard")

        else:

            return redirect("/authentication/admindashboard")    

        
class PasswordReset(LoginRequiredMixin, PasswordResetView):

    login_url = '/authentication/login/'
    template_name = 'registration/password_reset_form.html'
    # success_url = reverse_lazy('password_reset_done')
    next_page = "authentication/password_reset_done/"


class PasswordResetDone(LoginRequiredMixin, PasswordResetDoneView):

    login_url = '/authentication/login'
    template_name = 'registration/password_reset_done.html'
    next_page = "/attendance/login/"


class PasswordChange(LoginRequiredMixin, PasswordChangeView):

    login_url = '/authentication/login/'
    template_name = 'registration/password_change_form.html'
    # success_url = reverse_lazy('password_change_done')
    next_page = "authentication/password_change_done/"


class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):

    login_url = '/authentication/login/'
    template_name = 'registration/password_change_done.html'
    next_page = "/attendance/dashboard/"


class PasswordResetConfirm(LoginRequiredMixin, PasswordResetConfirmView):
    
    login_url = '/authentication/login/'
    template_name = 'registration/password_reset_confirm.html'
    # success_url = reverse_lazy('password_reset_complete')    
    next_page = "authenticaton/passwordresetcomplete/"


class PasswordResetComplete(LoginRequiredMixin, PasswordResetCompleteView):

    login_url = '/authentication/login/'
    template_name = 'registration/password_reset_complete.html'
    next_page = "/attendance/dashboard/"


class UserLogout(LoginRequiredMixin, LogoutView):

    login_url = '/authentication/login/'
    template_name="registration/logout.html"
    # redirect ="/authentication/login"
    next_page = "/authentication/login/"


@login_required
def home(request):

    return render(request, "home.html")


@login_required
def admin_dashboard(request):

    return render(request, "registration/admin_dashboard.html")


@login_required
def teacher_dashboard(request):

    return render(request, "registration/teacher_dashboard.html")


def register(request):

    """
    REGISTER VIEW
    register is the function used to sign up the user through AbstractUserForm which has some
    inbuilt fields.if form is valid then it will be saved in database.
    """

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('/authentication/login') 

    else:  

        form = RegisterForm()

    return render(request, "register.html", {"form" : form})    



# @login_required   
     
# class Dashboard(LoginRequiredMixin, TemplateView):
    
#     login_url = '/authentication/login/'
#     queryset = CustomUser.objects.all()
#     template_name = "dashboard.html"

class DeleteUser(LoginRequiredMixin, DeleteView):

    model = CustomUser
    template_name = "registration/delete_user.html"
    success_url = "/attendance/admindashboard"

    def get(self, request, args, *kwargs):
        return render(request, self.template_name)

    def delete(self, request, user_id, pk, *args, **kwargs):

        filter_user = CustomUser.objects.get(id = user_id).first()
        filter_user.delete()
        return redirect("attendance/admindashboard")



