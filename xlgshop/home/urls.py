from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view/categories/<str:category_name>", views.categories, name="categories"),
    path("view/details/<str:item_id>", views.details, name="details"),
]