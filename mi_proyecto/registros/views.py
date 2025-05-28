from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Registro
from .forms  import RegistroForm

@login_required
def lista_registros(request):
    items = Registro.objects.all().order_by('-fecha')
    return render(request, 'registros/lista.html', {'items': items})

def crear_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroForm()
    return render(request, 'registros/formulario.html', {'form': form})
