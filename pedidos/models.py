from django.db import models
from carrito.models import Carrito

class Pedido(models.Model):
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE, related_name="pedido")
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=25,
        choices=[("PENDIENTE", "Pendiente"), ("ENVIADO", "Enviado"), ("ENTREGADO", "Entregado")],
        default="PENDIENTE"
    )

    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def total(self):
        return self.carrito.total()

    def __str__(self):
        return f"Pedido #{self.id} del carrito #{self.carrito.id}"
class ImagenPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='pedidos/')

    class Meta:
        verbose_name = "Imagene"
        verbose_name_plural = "Imagenes"

    def __str__(self):
        return f"imagenes del pedido {self.pedido.pk}"
