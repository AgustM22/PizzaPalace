from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="offer"),
    path("filter", views.filter, name="filter"),
    path("<int:offer_id>", views.offerview, name="offerview")
]