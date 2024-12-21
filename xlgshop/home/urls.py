from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("details/<str:item_id>", views.details, name="details"),
]