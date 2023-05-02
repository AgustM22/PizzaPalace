from django.urls import path
from . import views

# Localhost:8000/Homepage
urlpatterns = [
    path("", views.main, name="main"),
]