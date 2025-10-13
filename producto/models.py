from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to="media-productos/")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    
    CATEGORIAS = [
        ("FIGURA", "Figura Decorativa"),
        ("PIEZA", "Pieza Funcional"),
        ("PERSONALIZADO", "Diseño Personalizado")
    ]
    categorias = models.CharField(max_length=255, choices=CATEGORIAS, default="PIEZA")
    disponible = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre