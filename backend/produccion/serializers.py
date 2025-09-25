from .models import Produccion, ProduccionProducto
from rest_framework import serializers

class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = "__all__"

class ProduccionProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduccionProducto
        fields = "__all__"