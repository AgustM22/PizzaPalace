from django.urls import path
from . import views

# Localhost:8000/login
urlpatterns = [
    path("", views.main, name="login"),
]