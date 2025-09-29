from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Productos
from .serializers import ProdusctoSerializer
# Create your views here.

class ProductoView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                productos = Productos.objects.get(pk=pk)
                serializer = ProdusctoSerializer(productos)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Productos.DoesNotExist:
                return Response({"error": "El producto no ha sido encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            productos = Productos.objects.all()
            serializer = ProdusctoSerializer(productos, many=True)

    def post(self, request):
        serializer = ProdusctoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        try:
            productos = Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            return Response({"error": "El producto no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProdusctoSerializer(productos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error", "El producto no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            productos = Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            return Response({"error": "El producto no fue encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        productos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    