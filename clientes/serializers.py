from rest_framework import serializers
from .models import DatosPersonales, DatosEntrega, DatosFactura

class PersonalSerializer(serializers.ModelSerializer):
    model = DatosPersonales
    fields = "__all__"

class EntregaSerializer(serializers.ModelSerializer):
    model = DatosEntrega
    fields = "__all__"

class FacturaSerializer(serializers.ModelSerializer):
    model = DatosFactura
    fields = "__all__"