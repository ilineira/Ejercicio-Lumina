from src.sistema.Sistema import Sistema
from src.entidades.Cliente import Cliente
import unittest


class SistemaTests(unittest.TestCase):

    def setUp(self) -> None:
        self.cliente = Cliente(1, '9 de Julio', 'Responsable Inscripto', 'Dni', 123456789)
        self.sistema = Sistema.instance()
