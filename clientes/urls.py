from django.urls import path
from .views import PersonalView, EntregaView, FacturaView

urlpatterns = [
    path("cliente/", PersonalView.as_view(), name="cliente-list"),
    
]