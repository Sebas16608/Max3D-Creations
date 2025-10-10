from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# Funcion por si los datos no existen
def notexist():
    return {"error": "Los datos no existen"}

class UserView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                users = User.objects.get(pk=pk)
                serializer = UserSerializer(users)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            users = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    