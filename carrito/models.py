from django.db import models
from django.core.exceptions import ValidationError
from user.models import User
from producto.models import Producto

class Carrito(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="carrito"
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("FINALIZADO", "Finalizado"),
        ("ABANDONADO", "Abandonado")
    ]