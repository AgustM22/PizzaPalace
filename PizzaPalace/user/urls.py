from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path
from . import views


urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("login" , LoginView.as_view(template_name="user/login.html"), name ="login"),
    path("logout", LogoutView.as_view(next_page="login"),name="logout"), #Yet to be implemented
    path("profile", views.profile, name="profile")
]