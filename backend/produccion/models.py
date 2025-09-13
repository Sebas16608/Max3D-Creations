from django.db import models
from pedidos.models import Pedido
from producto.models import Productos
# Create your models here.

class ProduccionProducto(models.Model):
    produccion = models.ForeignKey('Produccion', on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Produccion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="producciones")
    producto = models.ManyToManyField(Productos, through=ProduccionProducto)
    
    ESTADOS = [
        ("PENDIENTE", "Pendientes"),
        ("EN PROCESO", "En Proceso"),
        ("TERMINADO", "Terminado"),
        ("CANCELADO", "Cancelado"),
    ]
    estado = models.CharField(max_length=255, choices=ESTADOS)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField()
    nota_interna = models.TextField(blank=True, null=True)