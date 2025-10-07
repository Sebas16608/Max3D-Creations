from .models import Carrito
from rest_framework import serializers

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = "__all__"