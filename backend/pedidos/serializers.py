from rest_framework import serializers
from .models import Pedido, PedidoProductos

class PedidoSerializer(serializers.ModelSerializer):
    model = Pedido
    fields = "__all__"

class PedidoProducto(serializers.ModelSerializer):
    model = PedidoProductos
    fields = "__all__"