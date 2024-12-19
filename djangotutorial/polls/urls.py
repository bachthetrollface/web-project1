from django.urls import path
from . import views

"""
Path: <datatype:parameter_name> + function to execute with given parameters
"""
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail")
]