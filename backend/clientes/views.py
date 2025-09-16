from django.shortcuts import render
from .models import Datos_Personales, Datos_Entrega
from .serializers import PersonalSerializers, EntregaSerializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
class PersonalView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                datos_personales = Datos_Personales.objects.get(pk=pk)
                serializer = PersonalSerializers(datos_personales)
                return Response(serializer.data)
            except Datos_Personales.DoesNotExist:
                return Response({"error", "Los datos del cliente no se encuentran"}, status=status.HTTP_404_NOT_FOUND)
        else:
            datos_personales = Datos_Personales.objects.all()
            serializer = PersonalSerializers(datos_personales)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = PersonalSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            datos_personales = Datos_Personales.objects.get(pk=pk)
        except Datos_Personales.DoesNotExist:
            return Response({"error": "Los datos del cliente no se encuentran"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonalSerializers(datos_personales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            datos_personales = Datos_Personales.objects.get(pk=pk)
        except Datos_Personales.DoesNotExist:
            return Response({"error": "Los datos del cliente no se encuntran"}, status=status.HTTP_404_NOT_FOUND)
        
        datos_personales.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)