from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("checkout", views.checkout, name="checkout"),
    path("addcart", views.addToCart, name="addtocart"),
    path("getcart", views.getcart, name="getcart"),
    path("deletecart", views.deletecart, name="deletecart"),
    path("editcart", views.editcart, name="editcart")
]