from .models import Carrito
from .serializers import CarritoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# Funcion por si los datos no se encuentran
def notexist():
    return {"error": "Los datos no fueron encontrados"}

class CarritoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                carritos = Carrito.objects.get(pk=pk)
                serializer = CarritoSerializer(carritos)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Carrito.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            carritos = Carrito.objects.all()
            serializer = CarritoSerializer(carritos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = CarritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            carritos = Carrito.objects.get(pk=pk)
        except Carrito.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        serializer = CarritoSerializer(carritos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            carritos = Carrito.objects.get(pk=pk)
        except Carrito.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        carritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


            