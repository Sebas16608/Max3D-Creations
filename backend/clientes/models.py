from django.db import models

# Create your models here.
class Datos_Personales(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=25)
    telefono_alterno = models.CharField(max_length=25)

class Datos_Entrega(models.Model):
    direccion = models.TextField()
    codigo_acceso = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)

