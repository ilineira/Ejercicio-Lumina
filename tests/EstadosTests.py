from src.entidades.estadosDePedido.EstadoPendiente import EstadoPendiente
from src.entidades.estadosDePedido.EstadoFacturado import EstadoFacturado
import unittest


class EstadosTests(unittest.TestCase):

    def test01CreoEstadoPendiendeYVerificoEstado(self):
        estado = EstadoPendiente()
        self.assertEqual(estado.getEstado(), 'Pendiente')

    def test02CreoEstadoFacturadoYVerificoEstado(self):
        estado = EstadoFacturado()
        self.assertEqual(estado.getEstado(), 'Facturado')

    def test03CreoEstadoPendienteYFacturo(self):
        estado = EstadoPendiente()
        estado = estado.facturar()
        self.assertEqual(estado.__class__, EstadoFacturado().__class__)

    def test04CreoEstadoFacturadoYFacturo(self):
        estado = EstadoFacturado()
        estado = estado.facturar()
        self.assertEqual(estado.__class__, EstadoFacturado().__class__)
