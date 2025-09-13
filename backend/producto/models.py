from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    """
    STOCK = [
    ("DISPONIBLE", "Disponible"),
    ("FUERA", "Fuera de Stock"),
    ]
    stock = models.CharField(max_length=255, choices=STOCK)
    """
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="")
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    """
    Todo lo que es categoria, crear modelo aparte mas adelante porque van a haber mas, mientras vaya
    escalando el proyecto
    """
