from django import forms
from .models import Registro, Venta, Cliente
from datetime import date


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['nombre', 'descripcion']

class VentaForm(forms.ModelForm):
    class Meta:
        model  = Venta
        fields = ['cliente', 'control', 'licencia', 'fecha', 'estado']
        labels = {
            'control' : 'Datos del equipo (Control + U)',
            'estado' : 'Estado del pago',
            'cliente' : 'Numero del Cliente',
            'fecha' : 'Fecha de la entrega',
            'licencia' : 'Licencia Serial',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.is_bound:
            self.fields['fecha'].initial = date.today()

class ClienteForm(forms.ModelForm):
    class Meta:
        model  = Cliente
        fields = ['telefono', 'nombre']
        widgets = {
            'telefono': forms.TextInput(attrs={'placeholder': '987654321'}),
            'nombre':   forms.TextInput(attrs={'placeholder': 'Juan Pérez'}),
        }