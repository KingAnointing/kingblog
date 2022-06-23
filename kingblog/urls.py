from .views import *
from django.urls import path

urlpatterns = [
    path("/", PostListView.as_view(), name="post_list"),
    path("/whoami",AboutView.as_view() ,name='whoami'),
    path("blog/<int:pk>", PostDetailView.as_view(), name="post_detail")
]
