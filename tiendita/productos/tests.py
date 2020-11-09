import unittest
from productos.models import Producto


class testProducto(unittest.TestCase):

    def test_crear_bebiba(self):
        producto = Producto.objects.create(numero= 99,
                                       nombre='COCACOLA',
                                       precio= 1200,
                                       stock= 900,
                                       tipo='Bebida',
                                       activo=1
                                       )
        producto.save()

        self.assertTrue(producto,True)

    def test_crear_cabrita(self):
        producto = Producto.objects.create(numero=67,
                                           nombre='CABRITA GRANDE',
                                           precio=15000,
                                           stock=100,
                                           tipo='Cabrita',
                                           activo=1
                                           )
        producto.save()

        self.assertTrue(producto, True)