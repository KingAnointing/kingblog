from .views import *
from django.urls import path

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("whoami/",AboutView.as_view() ,name='whoami'),
    path("postadmin/", PostAdminView.as_view(), name="post_admin"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new", CreatePostView.as_view(), name="create_post"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="edit_post"),
    # path("post/<int:id>/edit/", PostUpdateView.as_view(), name="update_post"),
    # path("post/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("drafts/", DraftListView.as_view(), name="post_draft_list"),
    path("post/<slug:slug>/comment/", addCommentToPost, name="add_comment"),
    path("comment/<int:pk>/approve/", commentApprove, name="approve_comment"),
    path("comment/<int:pk>/remove/", commentRemove, name="remove_comment"),
    path("post/<int:pk>/publish/", postPublish, name="publish_post"),
    path("KingAnointing/resume-pdf/", pdfView, name="pdf_view"),
]
