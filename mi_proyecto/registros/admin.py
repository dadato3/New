from django.contrib import admin
from .models import Registro

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha')
    search_fields = ('nombre',)
