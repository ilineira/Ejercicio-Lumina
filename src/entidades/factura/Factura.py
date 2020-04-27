from src.entidades.factura.NotaDeCredito import NotaDeCredito
from entidades.factura.componentes.Cabecera import Cabecera
from entidades.factura.componentes.Detalle import Detalle
from entidades.factura.componentes.Pie import Pie


class Factura:

    def __init__(self, pedido, numeroDeFactura):
        self.cliente = pedido.getCliente()
        self.cabecera = Cabecera(pedido, numeroDeFactura)
        self.detalle = Detalle(pedido)
        self.pie = Pie(self.detalle)

    def anular(self):
        return NotaDeCredito(self.cliente, self.cabecera, self.pie)

    def generarReporte(self):
        linea = '{0}-{1}-{2}-{3}-{4}-{5}\n'.format(self.cliente.getNumeroDeCliente(),
                                                 self.cliente.getTipoDeDocumento(),
                                                 self.cabecera.getLetra(),
                                                 self.cabecera.getNumeroDeFactura(),
                                                 self.cabecera.getFechaDeEmision(),
                                                 self.pie.getMonto())
        return linea
