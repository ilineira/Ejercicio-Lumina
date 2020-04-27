import datetime


class Cabecera:

    def __init__(self, pedido, numeroDeFactura):
        self.fechaDeEmision = datetime.datetime.now().date()
        self.numeroDeFactura = numeroDeFactura
        self.codigoDeEmision = ''
        self.letra = pedido.getCliente().getCondicionImpositiva().getLetra()
        self.cliente = pedido.cliente.getNumeroDeCliente()
        """Ver si cliente es Cliente o numero de cliente(creo que la segunda opcion es la correcta"""

    def getCodigoDeEmision(self):
        return self.codigoDeEmision

    def getNumeroDeFactura(self):
        return self.numeroDeFactura

    def getLetra(self):
        return self.letra

    def getCliente(self):
        return self.cliente

    def getFechaDeEmision(self):
        return self.fechaDeEmision
