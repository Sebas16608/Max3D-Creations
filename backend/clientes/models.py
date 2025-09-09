from django.db import models

# Create your models here.
class Cliente(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.TextField()
    