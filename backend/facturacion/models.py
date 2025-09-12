from django.db import models
from clientes.models import Datos_Personales
# Create your models here.
class Datos_Factura(models.Model):
    nombre = models.CharField(max_length=255)
    IDENTIFICACIONES = [
        ("CUI", "CUI"),
        ("PASAPORTE", "Pasaporte"),
        ("NIT", "NIT"),
    ]
    identificacion = models.CharField(max_length=200, choices=IDENTIFICACIONES)

    def opcion(self):
        if self.identificacion == "CUI":
            return "Numero de CUI"
        elif self.identificacion == "PASAPORTE":
            return "Numero de Pasaporte"
        elif self.identificacion == "NIT":
            return "Numero de NIT"
        else:
            return "Por favor llenar el campo"
    
    class Meta:
        verbose_name = "Dato de facturacion"
        verbose_name_plural = "Datos de facturacion"

    def __str__(self):
        return f"{self.nombre} - {self.identificacion}"
    

class Items_factura(models.Model):
    factura = models.ForeignKey(Datos_Factura, on_delete=models.CASCADE, name="items" )
    producto = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.producto} x {self.cantidad}"

    