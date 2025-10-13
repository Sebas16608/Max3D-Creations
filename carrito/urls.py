from .views import CarritoView, CarritoItemView
from django.urls import path

urlpatterns = [
    path("carrito/", CarritoView.as_view(), name="carrito-list"),
    path("carrito/<int:pk>/", CarritoView.as_view(), name="carrito-detail"),
    path("carrito-item/", CarritoItemView.as_view(), name="item-list"),
    path("carrito-item/<int:pk>/", CarritoItemView.as_view(), name="item-detail")
]