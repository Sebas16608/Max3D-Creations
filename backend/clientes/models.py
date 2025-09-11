from django.db import models

# Create your models here.
class Datos_Personales(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=25)
    telefono_alterno = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Dato personal"
        verbose_name_plural = "Datos personales"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Datos_Entrega(models.Model):
    direccion = models.TextField()
    codigo_acceso = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Dato de entrega"
        verbose_name_plural = "Datos de entrega"

    def __str__(self):
        return f"{self.direccion} {self.municipio} {self.departamento}"
