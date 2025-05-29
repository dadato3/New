from django.urls import path
from . import views

urlpatterns = [
    path('',         views.dashboard, name='dashboard'),
    path('ventas/',views.ventas,    name='ventas'),
    path('clientes/',views.clientes,  name='clientes'),
    path('usuarios/',views.usuarios,  name='usuarios'),
    path('registros/',views.registros,  name='registros'),
]
