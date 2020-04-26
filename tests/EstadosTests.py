from src.entidades.estados.EstadoPendiente import EstadoPendiente
from src.entidades.estados.EstadoListoParaDespachar import EstadoListoParaDespachar
from src.entidades.Pedido import Pedido
from src.entidades.Cliente import Cliente
import unittest


class EstadosTests(unittest.TestCase):

    def setUp(self) -> None:
        self.pedido = Pedido(123, Cliente(
            1,
            '9 de Julio',
            'Responsable Inscripto',
            'Dni',
            123456789
        ))

    def test01CreoEstadoPendiendeYVerificoEstado(self):
        estado = EstadoPendiente()
        self.assertEqual(estado.getEstado(), 'Pendiente')

    def test02CreoEstadoFacturadoYVerificoEstado(self):
        estado = EstadoListoParaDespachar()
        self.assertEqual(estado.getEstado(), 'Listo para despachar')

    def test03CreoEstadoPendienteYFacturo(self):
        estado = EstadoPendiente()
        self.assertEqual(estado.facturar(self.pedido).__class__, EstadoListoParaDespachar)


    def test04CreoEstadoFacturadoYFacturo(self):
        estado = EstadoListoParaDespachar()
        self.assertEqual(estado.facturar(self.pedido).__class__, EstadoListoParaDespachar)
