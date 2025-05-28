# registros/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',    views.lista_registros,  name='lista_registros'),
    path('nuevo/', views.crear_registro, name='crear_registro'),
]
