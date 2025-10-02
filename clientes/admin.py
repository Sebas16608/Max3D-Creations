from django.contrib import admin
from .models import DatosPersonales, DatosEntrega, DatosFactura
# Register your models here.
admin.site.register(DatosPersonales)
admin.site.register(DatosEntrega)
admin.site.register(DatosFactura)