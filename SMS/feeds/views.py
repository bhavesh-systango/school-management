
import datetime
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from requests import post, request
from django.views.generic import DeleteView
from feeds.forms import FeedForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import FormView


class PostForm(LoginRequiredMixin, FormView):

    template_name = "feed/admin_post_form.html"
    form_class = FeedForm
    success_url = "/authentication/admindashboard"

    def post(self, request, *args, **kwargs):
      
        form = self.get_form()
        print(request.user.id)
        print("*****************")

        # filter_post = Post.objects.filter(user = request.user.id,user__user_type = 3 ).first()
        
        filter_post = Post()
        filter_post.user = request.user
        filter_post.title = request.POST["title"] 
        filter_post.content = request.POST["content"]
        filter_post.created_on = datetime.datetime.now()
        filter_post.save()

        return redirect("/attendance/dashboard")


class PostView(LoginRequiredMixin, ListView):
    
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):

        print(request.user.id)
        post_filter =  Post.objects.all()
        print(post_filter)

        return render(request,"feed/list_post.html",{'post_list' : post_filter})


# class DisplayPost(LoginRequiredMixin, DetailView):

#     pass


class DeletePost(LoginRequiredMixin, DeleteView):

    template_name = "feed/delete_post.html"
    model = Post
    success_url = "/attendance/admindashbioard"

    def get(self, request, args, *kwargs):
        return render(request, self.template_name)

    def delete(self,post_id,  request, pk, *args, **kwargs):
        
        # delete_post = Post.objects.
        feeds = Post.objects.filter( id = post_id).first()
        feeds.delete()
        return redirect("attendance/admindashboard")


