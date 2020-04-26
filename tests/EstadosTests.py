from src.entidades.estadosDePedido.EstadoPendiente import EstadoPendiente
from src.entidades.estadosDePedido.EstadoFacturado import EstadoFacturado
from src.entidades.Pedido import Pedido
import unittest


class EstadosTests(unittest.TestCase):

    def test01CreoEstadoPendiendeYVerificoEstado(self):
        estado = EstadoPendiente()
        self.assertEqual(estado.getEstado(), 'Pendiente')

    def test02CreoEstadoFacturadoYVerificoEstado(self):
        estado = EstadoFacturado()
        self.assertEqual(estado.getEstado(), 'Facturado')

    def test03CreoEstadoPendienteYFacturo(self):
        pedido = Pedido()
        estado = EstadoPendiente()
        estado.facturar(pedido)
        self.assertEqual(estado.__class__, EstadoFacturado.__class__)

    def test04CreoEstadoFacturadoYFacturo(self):
        estado = EstadoFacturado()
        estado = estado.facturar()
        self.assertEqual(estado.__class__, EstadoFacturado.__class__)
