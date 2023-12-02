from django.urls import path
from .views import obtener_clima

urlpatterns = [
    path('obtener-clima/', obtener_clima, name='obtener_clima'),
]
