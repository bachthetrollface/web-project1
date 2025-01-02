from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view/categories/<str:category_name>", views.categories, name="categories"),
    path("view/details/<str:item_id>", views.details, name="details"),
    path("query", views.query, name="query"),
    path("login", views.log_in, name="login"),
    path("logout", views.log_out, name="logout"),
    path("register", views.register, name="register"),
    path("about", views.about, name="about")
]