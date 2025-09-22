from django.shortcuts import render
from .serializers import PedidoSerializer, PedidoProductoSerializer
from .models import Pedido, PedidoProductos
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
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

    def post(self, request):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            pedidos = Pedido.objects.get(pk=pk)
        except Pedido.DoesNotExist:
            return Response({"error": "El pedido no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PedidoSerializer(pedidos, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            pedidos = Pedido.objects.get(pk=pk)
        except Pedido.DoesNotExist:
            return Response({"error": "No se encontro el pedido"}, status=status.HTTP_404_NOT_FOUND)
        pedidos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PedidoProductoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                pedido_productos = PedidoProductos.objects.get(pk=pk)
                serializer = PedidoProductoSerializer(pedido_productos)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except PedidoProductos.DoesNotExist:
                return Response({"error": "El producto del pedido no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            pedido_productos = PedidoProductos.objects.all()
            serializer = PedidoProductoSerializer(pedido_productos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PedidoProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            pedido_productos = PedidoProductos.objects.get(pk=pk)
        except PedidoProductos.DoesNotExist:
            return Response({"error": "El producto del pedido no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PedidoProductoSerializer(pedido_productos, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            pedido_productos = PedidoProductos.objects.get(pk=pk)
        except PedidoProductos.DoesNotExist:
            return Response({"error": "No se encontro el producto del pedido"}, status=status.HTTP_404_NOT_FOUND)
        pedido_productos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)