from dataclasses import fields
from django import forms
from .models import Post


class FeedForm(forms.Form):
    
    title = forms.CharField(label = "Title", max_length = 20)
    content = forms.CharField(widget=forms.Textarea(), max_length = 200)

    class Meta:

        model = Post
        fields =["title", "content"]