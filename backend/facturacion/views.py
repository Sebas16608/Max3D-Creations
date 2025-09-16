from django.shortcuts import render
from facturacion.serializers import DatosSerializer, ItemsSerializer
from .models import Datos_Factura, Items_factura
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

"""
Datos API
"""
class DatosView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                datos = Datos_Factura.objects.get(pk=pk)
                serializer = DatosSerializer(datos)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Datos_Factura.DoesNotExist:
                return Response({"error": "Los datos de la Factura no se encuentran"},status=status.HTTP_404_NOT_FOUND)
        else:
            datos = Datos_Factura.objects.all()
            serializer = DatosSerializer(datos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
"""
Items API
"""
class ItemsView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                items = Items_factura.objects.get(pk=pk)
                serializer = ItemsSerializer(items)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Items_factura.DoesNotExist:
                return Response({"error": "Los items de la factura no se encuentran"}, status=status.HTTP_404_NOT_FOUND)
        else:
            items = Items_factura.objects.all()
            serializer = ItemsSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)