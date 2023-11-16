from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("inicio/", views.inicio, name="inicio"),
    path("inicio/api/", views.api, name="api"),
]