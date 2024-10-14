from django.urls import path
from . import views

app_name = "home_app"
urlpatterns = [
    path("", views.home, name="main"),
    path("sidebar", views.sidebar, name="sidebar_partial"),
    path("about", views.about, name="about"),
]
