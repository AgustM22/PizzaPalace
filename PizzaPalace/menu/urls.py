from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="menu"),
    path("filter", views.filter, name="filter"),
    path("<int:pizza_id>", views.pizzaview, name="pizzaview")
]