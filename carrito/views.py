from .models import Carrito, CarritoItem
from .serializers import CarritoItemSerializer, CarritoSerializer
from producto.models import Producto
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


def error_response(mensaje, status_code=status.HTTP_404_NOT_FOUND):
    return Response({"error": mensaje}, status=status_code)

class MiCarritoView(APIView):
    """
    Vista para obtener el carrito actual del usuario autenticado
    GET /api/mi-carrito/
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """ Obtiene o crea el carrito activo del usuario """
        carrito, created = Carrito.objects.get_or_create(
            usuario = request.user,
            estado = "ACTIVO"
        )