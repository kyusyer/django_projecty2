from django.urls import path

from . import views

app_name = "my_profile"
urlpatterns = [
    path("",views.index, name="index"),
    path("project", views.project, name="project")
]