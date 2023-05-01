from django.urls import path
from . import views

# Comment
# Hemmi comment
urlpatterns = [
    path("", views.main, name="main"),
]