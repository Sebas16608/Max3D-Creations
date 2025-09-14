from django.db import models
from clientes.models import Datos_Personales, Datos_Entrega
from producto.models import Productos
class Pedido(models.Model):
    cliente = models.ForeignKey(Datos_Personales, on_delete=models.CASCADE, related_name="pedidos")
    entrega = models.ForeignKey(Datos_Entrega, on_delete=models.CASCADE, related_name="pedidos_entrega")
    productos = models.ManyToManyField(Productos, through="PedidoProductos")
    cantidad = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)