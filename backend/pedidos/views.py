from django.shortcuts import render
from .serializers import PedidoSerializer, PedidoProductoSerializer
from .models import Pedido, PedidoProductos
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class PedidoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                pedidos = Pedido.objects.get(pk=pk)
                serializer = PedidoSerializer(pedidos)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Pedido.DoesNotExist:
                return Response({"error": "El pedido no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            pedidos = Pedido.objects.all()
            serializer = PedidoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
