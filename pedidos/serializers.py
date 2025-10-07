from .models import Pedido, ImagenPedido
from rest_framework import serializers

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Pedido
        fields = "__all__"

class ImagenPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenPedido
        fields = "__all__"