from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("addcart", views.addToCart, name="addtocart"),
    path("getcart", views.getcart, name="getcart"),
    path("editcart", views.editcart, name="editcart"),
    path("contactinformation", views.contactinformation, name="contactinformation"),
    path("checkcontactinformation", views.checkcontactinformation, name="checkcontactinformation"),
    path("creditcard", views.creditcard, name="creditcard"),
    path("checkcreditcard", views.checkcreditcard, name="checkcreditcard"),
    path("overview", views.overview, name="overview"),
    path("payonpickup", views.payonpickup, name="payonpickup"),
    path("deletecart", views.deletecart, name="deletecart")
]