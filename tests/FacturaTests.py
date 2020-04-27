from src.entidades.factura.Factura import Factura
from src.entidades.Pedido import Pedido
from src.entidades.Cliente import Cliente
from src.entidades.Producto import Producto
from src.entidades.factura.NotaDeCredito import NotaDeCredito
import unittest


class FacturaTests(unittest.TestCase):

    def setUp(self) -> None:
        self.pedido = Pedido(123, Cliente(
                    1,
                    '9 de Julio',
                    'Responsable Inscripto',
                    'Dni',
                    123456789
                ))
        self.pedido.agregarProducto(Producto(1, 'Nombre', 10), 20)
        self.factura = Factura(self.pedido, 1)

    def test01CreoFacturaGeneroReporte(self):
        lineaReporte = '{0}-{1}-{2}-{3}-{4}-{5}\n'.format(1, 'Dni', 'A', '',
                                                        self.factura.cabecera.getFechaDeEmision(),
                                                        self.factura.pie.getMonto())
        self.assertEqual(self.factura.generarReporte(), lineaReporte)

    def test02CreoFacturaYLaAnulo(self):
        self.assertEqual(self.factura.anular().__class__, NotaDeCredito)

    def test03CreoFacturaYVerificoCalculoDeMonto(self):
        """calculo -> precio unitario * cantidad * monto de IVA"""
        self.assertEqual(self.factura.detalle.getMontoDeIVA(), (10 * 20 * 10.05/100))


