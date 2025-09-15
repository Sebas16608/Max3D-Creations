from django.db import models
from clientes.models import Datos_Personales
from producto.models import Productos
# Create your models here.
class Carrito(models.Model):
    cliente = models.ForeignKey(Datos_Personales, on_delete=models.CASCADE, related_name="carritos")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

    def __str__(self):
        return f"Carrito de {self.cliente.nombre} ({'Activo' if self.activo else 'Cerrado'})"

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name="carritos")
    cantidad = models.IntegerField()

    class Meta:
        verbose_name = "Item carrito"
        verbose_name_plural = "Items carrito"

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

