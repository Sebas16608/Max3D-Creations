from django.urls import path
from clientes.views import EntregaView, PersonalView

urlpatterns = [
    path("cliente/", PersonalView.as_view(), name="cliente-list"),
    path("cliente/<int:pk>/", PersonalView.as_view(), name="cliente-detail"),
    path("entrega/", EntregaView.as_view(), name="entregas-list"),
    path("entrega/<int:pk>/", EntregaView.as_view(), name="entregas-detail"),
]