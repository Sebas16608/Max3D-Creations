from django.db import models
from clientes.models import DatosPersonales
from pedidos.models import Pedido
# Create your models here.
class Carrito(models.Model):
    pedido = models.ForeignKey(Pedido)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("FINALIZADO", "Finalizado")
    ]
    estado = models.CharField(max_length=25, choices=ESTADOS)

    def total(self):
        return sum(p.precio for p in self.pedido.all() if hasattr(p, "precio"))
    
    def __str__(self):
        return f"Carrito #{self.id} de {self.cliente}"
    
    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"