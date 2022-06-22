from . import views

from django.urls import path

urlpatterns = [
    path("",views.blog, name="blog"),
    path("blog/<str>",views.blogPost,name="blogpost"),
    path("/whoami",views.whoAmI,name='whoami')
]
