from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("addcart", views.addToCart, name="addtocart"),
    path("getcart", views.getcart, name="getcart"),
    path("deletecart", views.deletecart, name="deletecart")
]