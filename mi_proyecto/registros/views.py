from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VentaForm
from datetime import date

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
    return render(request, 'registros/registros.html')
