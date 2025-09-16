from django.urls import path
from .views import DatosView, ItemsView

urtpatterns = [
    path("datos/", DatosView.as_view(), name="datos-list"),
    path("datos/<int:pk>/", DatosView.as_view(), name="datos-detail"),
    path("items/", ItemsView.as_view(), name="items-list"),
    path("items/<int:pk>/", ItemsView.as_view(), name="items-detail")
]