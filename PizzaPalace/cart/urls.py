from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("contactinformation", views.contactinformation, name="contactinformation"),
    path("addcart", views.addToCart, name="addtocart"),
    path("getcart", views.getcart, name="getcart"),
    path("checkcreditcard", views.checkcreditcard, name="checkcreditcard"),
    path("creditcard", views.creditcard, name="creditcard"),
    path("editcart", views.editcart, name="editcart"),
    path("checkcontactinformation", views.checkcontactinformation, name="checkcontactinformation"),
    path("overview", views.overview, name="overview"),
]