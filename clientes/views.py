from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonalSerializer, EntregaSerializer, FacturaSerializer
from .models import DatosPersonales, DatosEntrega, DatosFactura


# Funcion para cuando no existan los datos
def notexist():
    return {"error": "Los datos no fueron encontrado"}

class PersonalView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                personal = DatosPersonales.objects.get(pk=pk)
                serializer = PersonalSerializer(personal)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except DatosPersonales.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            personal = DatosPersonales.objects.all()
            serializer = PersonalSerializer(personal, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PersonalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)