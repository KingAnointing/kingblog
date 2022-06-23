from .views import *
from django.urls import path

urlpatterns = [
    path("/", PostListView.as_view(), name="post_list"),
    path("whoami/",AboutView.as_view() ,name='whoami'),
    path("blog/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("blog/new", CreatePostView.as_view(), name="create_blog"),
    path("post/<int:id>/edit/", PostUpdateView.as_view(), name="update_blog"),
]
