from rest_framework import serializers
from .models import Productos

class ProdusctoSerializer(serializers):
    class Meta:
        model = Productos
        fields = "__all__"

