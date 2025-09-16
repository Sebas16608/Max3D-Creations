from django.test import TestCase, Client
from django.urls import reverse
from clientes.models import Datos_Personales, Datos_Entrega

class URLTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Crear instancias para probar las URLs
        self.cliente = Datos_Personales.objects.create(nombre="Sebas")  # ajusta según campos reales
        self.entrega = Datos_Entrega.objects.create(direccion="Zona 1")  # ajusta según campos reales

    def test_cliente_list_url(self):
        url = reverse('cliente-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_cliente_detail_url(self):
        url = reverse('cliente-detail', args=[self.cliente.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_entrega_list_url(self):
        url = reverse('entregas-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_entrega_detail_url(self):
        url = reverse('entregas-detail', args=[self.entrega.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
