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
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            datos = Datos_Factura.objects.all()
            serializer = DatosSerializer(datos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
"""

"""