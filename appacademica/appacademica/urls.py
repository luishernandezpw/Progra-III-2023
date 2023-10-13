from django.contrib import admin
from django.urls import path
from appalumnos.views import saludo, miEdad, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('edad/<int:edad>/', miEdad),
     path('', index),
]
