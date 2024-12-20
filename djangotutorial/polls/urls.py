from django.urls import path
from . import views

"""
Path: <datatype:parameter_name> + function to execute with given parameters

name for paths for easier maintenance of namespaces in front-end
app_name to specify views belonging to which applications
"""

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail")
]