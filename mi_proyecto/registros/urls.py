from django.urls import path
from . import views

urlpatterns = [
    path('',         views.dashboard, name='registros'),
    path('registros/',views.registros,    name='registros'),
    path('ventas/',views.ventas,    name='ventas'),
    path('clientes/', views.clientes, name='clientes'),
    path('usuarios/',views.usuarios,  name='usuarios'),
    #sub rutas
    path('clientes/',                  views.clientes,           name='clientes_home'),
    path('clientes/crear/',            views.crear_cliente,      name='crear_cliente'),
    path('clientes/modificar/<str:telefono>/', views.modificar_cliente, name='modificar_cliente'),
    path('clientes/eliminar/<str:telefono>/',  views.eliminar_cliente,  name='eliminar_cliente'),
    # marcar pagado…
    path('ventas/<int:pk>/pagado/', views.marcar_pagado, name='marcar_pagado'),
]
