
from django.urls import path
from . import views
from .views import pregunta_ciudad, obtener_clima

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("confirmacion/", views.inicio_sesion_facial, name="confirmacion"),
    path("registro/", views.registro_facial, name="registro"),
    path("confirmacion/api/", views.api, name="api"),
    path('confirmacion/api/noticias/', views.noticias, name='noticias'),
    path('confirmacion/api/pregunta-ciudad/', pregunta_ciudad, name='pregunta_ciudad'),
    path('confirmacion/api/clima/', obtener_clima, name='obtener_clima'),
]

