from django.db import models

class Registro(models.Model):
    nombre     = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha      = models.DateField(auto_now_add=True)

class Venta(models.Model):
    cliente  = models.CharField(max_length=100)
    control  = models.CharField("Control U", max_length=50)
    licencia = models.CharField(max_length=100)
    fecha    = models.DateField()
    ESTADO_CHOICES = [
        ('pagado',    'Pagado'),
        ('pendiente', 'Pendiente'),
    ]
    estado   = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')


class Cliente(models.Model):
    telefono = models.CharField(
        "Teléfono", 
        max_length=20, 
        primary_key=True,
        help_text="Usado como ID único"
    )
    nombre = models.CharField("Nombre", max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.fecha})"
