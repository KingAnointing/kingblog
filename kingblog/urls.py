from .views import *
from django.urls import path

urlpatterns = [
    path("/whoami",AboutView.as_view() ,name='whoami'),
]
