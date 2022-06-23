from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from kingblog.models import Post, Comments
from .forms import *

# Create your views here.

class AboutView(TemplateView):
    template_name = "whoami.html"

class PostListView(ListView):
    model = Post
    context_object_name = ''
    template_name=''

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().orderby("-published_date"))
    
class PostDetailView(DetailView):
    model = Post
    template_name=''

class CreatePostView(CreateView,LoginRequiredMixin):
    model = Post
    template_name = ".html"
    login_url = '/login/'
    redirect_field_name = '/blog/post_detail/'
    form_class = PostForm
