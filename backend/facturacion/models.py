from django.db import models
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
        elif self.identificacion == "Pasaporte":
            return "Numero de Pasaporte"
        elif self.identificacion == "NIT":
            return "Numero de NIT"
        else:
            return "Por favor llenar el campo"