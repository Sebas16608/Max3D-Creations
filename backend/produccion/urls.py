from django.urls import path
from .views import ProduccionProductoView, ProduccionView

urlpatterns = [
    path("produccion/", ProduccionView.as_view(), name="produccion-list"),
    path("produccion/<int:pk>/", ProduccionView.as_view(), name="produccion-detail"),
    path("produccion-producto/", ProduccionProductoView.as_view(), name="produccion-producto-list"),
    path("produccion-product/<int:pk>/", ProduccionProductoView.as_view(), name="produccion-producto-detail")
]