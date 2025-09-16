from .models import Datos_Factura, Items_factura
from rest_framework import serializers

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos_Factura
        fields = "__all__"

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items_factura
        fields = "__all__"