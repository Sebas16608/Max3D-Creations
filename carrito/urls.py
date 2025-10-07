from .views import CarritoView
from django.urls import path

urlpatterns = [
    path("carrito/", CarritoView.as_view(), name="carrito-list"),
    path("carrito/<int:pk>/", CarritoView.as_view(), name="carrito-detail")
]