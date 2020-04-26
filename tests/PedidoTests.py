from src.entidades.Cliente import Cliente
from src.entidades.Producto import Producto
from src.entidades.Pedido import Pedido


import unittest


class PedidoTests(unittest.TestCase):

    def setUp(self) -> None:
        self.producto1 = Producto(1, 'Producto1', 10)
        self.producto2 = Producto(2, 'Producto2', 20)
        self.cliente = Cliente(1, '9 de Julio', 'Responsable Inscripto', 'Dni', 123456789)

    def test01CreoPedidoYVerificoCodigo(self):
        self.pedido = Pedido(123, self.cliente)
        self.assertEqual(self.pedido.getCodigo(), 123)

    def test02CreoPedidoYVerificoCliente(self):
        self.pedido = Pedido(123, self.cliente)
        self.assertEqual(self.pedido.getCliente(), self.cliente)

    def test03CreoPedidoYVerificoQueContengaUnicoProductoAgregado(self):
        self.pedido = Pedido(123, self.cliente)
        self.pedido.agregarProducto(self.producto1, 34)
        self.assertEqual(self.pedido.getDetalle(), [[self.producto1, 34]])

    def test04CreoPedidoYVerificoQueContengaLosDosProductosAgregados(self):
        self.pedido = Pedido(123, self.cliente)
        self.pedido.agregarProducto(self.producto1, 34)
        self.pedido.agregarProducto(self.producto2, 81)
        self.assertEqual(self.pedido.getDetalle(), [[self.producto1, 34], [self.producto2, 81]])

