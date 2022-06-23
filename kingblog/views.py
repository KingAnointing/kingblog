from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.utils import timezone

from kingblog.models import Post, Comments

# Create your views here.

class AboutView(TemplateView):
    template_name = "whoami.html"

class PostListView(ListView):
    model = Post
    context_object_name = ''
    template_name=''

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().orderby("-published_date"))
    