from django.urls import path
from .views import PedidoView

urlpatterns = [
    path("pedidos/", PedidoView.as_view(), name="pedidos-list"),
    path("pedidos/<int:pk>/", PedidoView.as_view(), name="pedidos-detail")
]