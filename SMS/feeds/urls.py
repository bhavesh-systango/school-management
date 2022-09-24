from django.urls import path
from .views import DeletePost, PostForm,PostView

app_name = "feeds"

urlpatterns = [
    
    path('feedform',PostForm.as_view(), name = "feed_form"),
    path('postview/',PostView.as_view(), name = "post_view"),
    path('deletepost/<int:post_id>/',DeletePost.as_view(), name = "delete_post"),

]
