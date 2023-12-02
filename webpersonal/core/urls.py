from django.contrib import admin
from django.urls import path, include
from core import views  # Asegúrate de que la importación sea correcta

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),  # Incluye las URLs de la aplicación core
    path('inicio/api/noticias/', views.noticias, name='noticias'),
]


