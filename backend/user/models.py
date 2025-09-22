from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    image = models.ImageField(null=True, default="avatar.svg")
    password = models.CharField(max_length=100, null=True)
    password2 = models.CharField(max_length=100, null=True)
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        return self.username
