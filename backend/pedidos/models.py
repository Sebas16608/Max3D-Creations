from django.db import models
from clientes.models import Datos_Personales, Datos_Entrega

class Pedido(models.Model):
    cliente = models.ForeignKey(Datos_Personales, on_delete=models.CASCADE, related_name="entrega")
    entrega = models.ForeignKey(Datos_Entrega, on_delete=models.CASCADE, related_name="entrega")
    fecha = models.DateField(auto_now_add=True)