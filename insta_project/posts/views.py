# posts/views.py
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(CreateView): # новый
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')