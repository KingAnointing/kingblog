from django import views
from .views import *
from django.urls import path

urlpatterns = [
    path("/", PostListView.as_view(), name="post_list"),
    path("whoami/",AboutView.as_view() ,name='whoami'),
    path("blog/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("blog/new", CreatePostView.as_view(), name="create_blog"),
    path("post/<int:id>/edit/", PostUpdateView.as_view(), name="update_blog"),
    path("post/<int:id>/edit/", PostUpdateView.as_view(), name="update_blog"),
    # path("post/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("drafts/<int:id>/", DraftListView.as_view(), name="draft_list"),
    path("post/<int:pk>/comment/", addCommentToPost, name="add_comment"),
    path("comment/<int:pk>", views.commentApprove, name="comment_approve"),
    path("comment/<int:pk>", commentRemove, name="remove_comment"),
    path("post/<int:pk>/publish", postPublish, name="publish_post")
]
