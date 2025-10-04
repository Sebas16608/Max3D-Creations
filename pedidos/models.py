from django.db import models

# Create your models here.
class Pedido(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class ImagenPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='pedidos/')