from django.db import models

# Create your models here.
class DatosPersonales(models.Model):
    nombre = models.CharField(max_length=255, blank=False)
    apellido = models.CharField(max_length=255, blank=False)
    telefono = models.CharField(max_length=100, blank=False)
    telefono_alterno = models.CharField(max_length=100, blank=True)
    email = models.EmailField()


class DatosEntrega(models.Model):
    direccion = models.TextField()
    codigo_de_acceso = models.CharField(max_length=100)
    departamento = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)

class DatosFactura(models.Model):
    nombre = models.CharField(max_length=255, blank=False)
    IDENTIFICACIONES = [
        #("NIT", "NIT"),
        ("CUI", "CUI"),
        ("PASAPORTE", "Pasaporte")
    ]
    identificacion = models.CharField(choices=IDENTIFICACIONES, max_length=25)
    no_identificacion = models.CharField(max_length=25, default="C/F")

    """
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.identificacion == "NIT" and not self.no_identificacion:
            raise ValidationError("Por favor ponga C/F o Consumidor Final")"""
        
    def identificador(self):
        #if self.identificacion == "NIT":
         #   return "Número de NIT"
        if self.identificacion == "CUI":
            return "Número de CUI/DPI"
        elif self.identificacion == "PASAPORTE":
            return "Número de Pasaporte"
        else:
            return "Por favor ingrese el numero de identificación"
        
"""
Por ahora el codigo estara con la funcion del NIT desactivada ya que el negocio debe estar registrado en el SAT para que podamos facturar con NIT. 😀
"""
        
    
