from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ClienteForm, VentaForm
from datetime import date
from django.db.models import Q
from .models import Venta, Cliente

@login_required
def dashboard(request):
    return render(request, 'registros/dashboard.html')

@login_required
def ventas(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas')   # recarga la misma página vaciando el formulario
    else:
        form = VentaForm(initial={'fecha': date.today()})
    return render(request, 'registros/ventas.html', {'form': form})

    

@login_required
def clientes(request):
    return render(request, 'registros/clientes.html')

@login_required
def usuarios(request):
    return render(request, 'registros/usuarios.html')

@login_required
def registros(request):
    # Recogemos parámetros de búsqueda
    q_cliente  = request.GET.get('cliente', '')
    q_fecha    = request.GET.get('fecha', '')
    q_licencia = request.GET.get('licencia', '')

    # Query inicial: todas las ventas, ordenadas por fecha descendente
    ventas = Venta.objects.all().order_by('-fecha')

    # Aplicamos filtros si vienen vacíos
    if q_cliente:
        ventas = ventas.filter(cliente__icontains=q_cliente)
    if q_fecha:
        ventas = ventas.filter(fecha=q_fecha)
    if q_licencia:
        ventas = ventas.filter(licencia__icontains=q_licencia)

    # Formulario vacío para registrar ventas si quieres mantenerlo
    form = VentaForm(initial={'fecha': date.today()})

    return render(request, 'registros/registros.html', {
        'ventas': ventas,
        'form': form,
        'q_cliente': q_cliente,
        'q_fecha': q_fecha,
        'q_licencia': q_licencia,
    })

@login_required
def marcar_pagado(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.estado = 'pagado'
        venta.save()
    return redirect('registros')   # nombre de la URL de tu listado


@login_required
def clientes_home(request):
    return render(request, 'registros/clientes.html')

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_home')
    else:
        form = ClienteForm()
    return render(request, 'registros/cliente_form.html', {
        'form': form,
        'titulo': 'Crear Cliente'
    })

@login_required
def modificar_cliente(request, telefono):
    cliente = get_object_or_404(Cliente, telefono=telefono)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes_home')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'registros/cliente_form.html', {
        'form': form,
        'titulo': 'Modificar Cliente'
    })

@login_required
def eliminar_cliente(request, telefono):
    cliente = get_object_or_404(Cliente, telefono=telefono)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes_home')
    return render(request, 'registros/cliente_confirm_delete.html', {
        'cliente': cliente
    })