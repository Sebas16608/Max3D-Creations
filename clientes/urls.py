from django.urls import path
from .views import PersonalView, EntregaView, FacturaView

urlpatterns = [
    path("cliente/", PersonalView.as_view(), name="cliente-list"),
    path("cliente/", PersonalView.as_view(), name="clientes-list"),
    path("cliente/<int:pk>/", PersonalView.as_view(), name="cliente-detail"),
    path("entrega/", EntregaView.as_view(), name="entregas-list"),
    path("entrega/<int:pk>/", EntregaView.as_view(), name="engtegas-detail"),
    path("factura/", FacturaView.as_view(), name="facturas-list"),
    path("facturas/<int:pk>/", FacturaView.as_view(), name="facturas-detail"),
    path("cliente/", PersonalView.as_view(), name="cliente-list"),
]