
from django.urls import path
from . import views
from .views import pregunta_ciudad, obtener_clima

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("inicio/", views.reconocimiento_facial, name="inicio"),
    path("inicio/api/", views.api, name="api"),
    path('inicio/api/noticias/', views.noticias, name='noticias'),
    path('inicio/api/pregunta-ciudad/', pregunta_ciudad, name='pregunta_ciudad'),
    path('inicio/api/clima/', obtener_clima, name='obtener_clima'),
]

