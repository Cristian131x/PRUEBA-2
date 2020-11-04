import unittest
from productos.models import Producto


class testProducto(unittest.TestCase):

    def test_crear_bebiba(self):
        producto = Producto.objects.create(numero= 900,
                                       nombre='COCACOLA',
                                       precio= 2000,
                                       stock= 100,
                                       tipo='Bebida',
                                       activo=1
                                       )
        producto.save()

        self.assertTrue(producto,True)

    def test_crear_cabrita(self):
        producto = Producto.objects.create(numero=9000,
                                           nombre='CABRITA GRANDE',
                                           precio=5000,
                                           stock=67,
                                           tipo='Cabrita',
                                           activo=1
                                           )
        producto.save()

        self.assertTrue(producto, True)