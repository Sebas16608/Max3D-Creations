from .models import Datos_Personales, Datos_Entrega
from rest_framework import serializers

class PersonalSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Datos_Personales
        fields = "__all__"

class EntregaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Datos_Entrega
        fields = "__all__"