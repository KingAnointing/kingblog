from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
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
    template_name = ''

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).orderby("-published_date")


class PostDetailView(DetailView):
    model = Post
    template_name = ''


class CreatePostView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = ".html"
    login_url = '/login/'
    redirect_field_name = '/blog/post_detail.html/'
    form_class = PostForm


class PostUpdateView(UpdateView):
    model = Post
    template_name = ".html"
    login_url = '/login/'
    redirect_field_name = '/blog/post_detail.html'
    form_class = PostForm


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    template_name = ".html"

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


def addCommentToPost(request,pk): 
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.post == post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})