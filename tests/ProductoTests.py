from src.entidades.Producto import Producto
import unittest


class ProductoTests(unittest.TestCase):

    def setUp(self) -> None:
        self.codigo = 1
        self.nombre = 'Nombre'
        self.precio = 10
        self.producto = Producto(self.codigo, self.nombre, self.precio)

    def test01CreoProductoYVerificoCodigo(self):
        self.assertEqual(self.producto.getCodigo(), self.codigo)

    def test02CreoProductoYVerificoNombre(self):
        self.assertEqual(self.producto.getNombre(), self.nombre)

    def test03CreoProductoYVerificoPrecio(self):
        self.assertEqual(self.producto.getPrecio(), self.precio)