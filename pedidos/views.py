from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pedido
from .serializers import PedidoSerializer
# Create your views here.

# Funcion
def notexits():
    return {"error": "Los Datos no Fueron encontrados"}

class Pedido(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                pedido = Pedido.objects.get(pk=pk)
                serializer = PedidoSerializer(pedido)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Pedido.DoesNotExist:
                return Response(notexits(), status=status.HTTP_404_NOT_FOUND)
        else:
            pedido = Pedido.objects.all()
            serializer = PedidoSerializer(pedido, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)