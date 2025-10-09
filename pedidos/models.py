from django.db import models
# from carrito.models import Carrito
# Create your models here.
class Pedido(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    #carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="pedido")

class ImagenPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='pedidos/')