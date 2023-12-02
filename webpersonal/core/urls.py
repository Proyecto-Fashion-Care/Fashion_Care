from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path("", views.home, name="home"),
    path("inicio/", views.inicio, name="inicio"),
    path("inicio/api/", views.api, name="api"),
    path('inicio/api/noticias.html/', views.noticias, name='noticias'),
    path('clima/', include('clima.urls')),
]