from .models import Pedido
from rest_framework import serializers

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Pedido
        fields = "__all__"