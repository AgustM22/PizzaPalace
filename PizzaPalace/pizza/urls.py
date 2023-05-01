from django.urls import path
from . import views

# Comment

urlpatterns = [
    path("", views.main, name="main"),
]