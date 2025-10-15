from django.db import models
from user.models import User
from producto.models import Producto

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carritos", default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("FINALIZADO", "Finalizado")
    ]
    estado = models.CharField(max_length=25, choices=ESTADOS, default="ACTIVO")

    def total(self):
        return sum(item.subtotal() for item in self.items.all())

    def __str__(self):
        return f"Carrito #{self.id} de {self.usuario}"
    
    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"


class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    def subtotal(self):
        return self.producto.precio * self.cantidad
        
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    
    class Meta:
        unique_together = ('carrito', 'producto')
