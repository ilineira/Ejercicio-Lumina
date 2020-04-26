from src.entidades.factura.NotaDeCredito import NotaDeCredito
from src.entidades.factura.Cabecera import Cabecera
from src.entidades.factura.Detalle import Detalle
from src.entidades.factura.Pie import Pie


class Factura:

    def __init__(self, pedido):
        self.cabecera = Cabecera(pedido)
        self.detalle = Detalle(pedido)
        self.pie = Pie(pedido)

    def anular(self):
        return NotaDeCredito(self.cabecera, self.pie)