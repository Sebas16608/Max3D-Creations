from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Produccion, ProduccionProducto
from .serializers import ProduccionSerializer, ProduccionProductoSerializer
from rest_framework import status

class ProduccionView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                producciones = Produccion.objects.get(pk=pk)
                serializer = ProduccionSerializer(producciones)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Produccion.DoesNotExist:
                return Response({"error": "La produccion no fue encontrada"}, status=status.HTTP_404_NOT_FOUND)
        else:
            producciones = Produccion.objects.all()
            serializer = ProduccionSerializer(producciones, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
