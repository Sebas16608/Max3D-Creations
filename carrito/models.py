from django.db import models
from user.models import User
# from producto.models import Producto
# Create your models here.
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carrito")
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

# Para manejar los items que vaya a contener el carrito
class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")
    # producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    """
    def subtotal(self):
        return self.producto.precio * self.cantidad
        
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"""