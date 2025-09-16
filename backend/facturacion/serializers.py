from .models import Datos_Factura, Items_factura
from rest_framework import serializers

class DatosView(serializers.ModelSerializer):
    class Meta:
        model = Datos_Factura
        fields = "__all__"

class ItemsView(serializers.ModelSerializer):
    class Meta:
        model = Items_factura
        fields = "__all__"