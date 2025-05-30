from django import forms
from .models import Registro, Venta, Cliente, Usuario
from datetime import date
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin



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

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model  = Usuario
        fields = ['username', 'role', 'password1', 'password2']
        widgets = {
            'role': forms.Select(attrs={'class':'form-control'}),
        }

class UsuarioChangeForm(UserChangeForm):
    password = None  # ocultamos el campo password en edición
    class Meta:
        model  = Usuario
        fields = ['username', 'role']
        widgets = {
            'role': forms.Select(attrs={'class':'form-control'}),
        }

@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'role', 'is_staff', 'is_active')
    list_filter  = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None,               {'fields': ('username', 'password')}),
        ('Información personal', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Roles y permisos',   {
            'fields': ('role', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Fechas',            {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'role', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('username', 'role')
    ordering = ('username',)