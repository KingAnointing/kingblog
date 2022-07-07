from urllib import response
from django.forms import SlugField
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from kingblog.models import Post, Comment
from .forms import *

# Create your views here.


class PostAdminView(TemplateView):
    template_name = "post_admin.html"


class AboutView(TemplateView):
    template_name = "whoami.html"


class PostListView(ListView):
    model = Post
    # context_object_name = ''
    # template_name = 'blog/templates/blog/post_list.html'
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")


class PostDetailView(DetailView):
    model = Post


class CreatePostView(CreateView, LoginRequiredMixin):
    model = Post
    # template_name = ".html"
    login_url = '/login/'
    redirect_field_name = '/kingblog/post_detail.html/'
    form_class = PostForm


class PostUpdateView(UpdateView):
    model = Post
    # template_name = ".html"
    login_url = '/login/'
    redirect_field_name = '/kingblog/post_detail.html'
    form_class = PostForm


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'kingblog/post_list.html'
    model = Post
    # template_name = ".html"

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


def addCommentToPost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'kingblog/comment_form.html', {'form': form})


@login_required
def commentApprove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', slug=comment.post.slug)


@login_required
def commentRemove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_slug = comment.post.slug
    comment.delete()
    return redirect('post_detail', slug=post_slug)


@login_required
def postPublish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def pdfView(request):
    with open('/home/kinganointing/Documents/djangoproject/blog/kingblog/static/resume/AdetoyeAnointingAdefemi_Resume.pdf','rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition']= 'inline;filename=AdetoyeAnointingAdefemi_Resume.pdf'
        return response