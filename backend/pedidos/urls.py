from django.urls import path
from .views import PedidoView, PedidoProductoView

urlpatterns = [
    path('pedidos/', PedidoView.as_view(), name='pedidos_list_create'),
    path('pedidos/<int:pk>/', PedidoView.as_view(), name='pedidos_detail'),
    path('pedido-productos/', PedidoProductoView.as_view(), name='pedido_productos_list_create'),
    path('pedido-productos/<int:pk>/', PedidoProductoView.as_view(), name='pedido_productos_detail'),
]