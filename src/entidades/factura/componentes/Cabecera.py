import datetime


class Cabecera:

    def __init__(self, pedido):
        self.fechaDeEmision = datetime.datetime.now().date()
        self.numeroDeFactura = ''
        self.codigoDeEmision = ''
        self.letra = pedido.cliente.getCondicionImpositiva().getLetra()
        self.cliente = pedido.cliente.getNumeroDeCliente()
        """Ver si cliente es Cliente o numero de cliente(creo que la segunda opcion es la correcta"""

    def getCodigoDeEmision(self):
        return self.codigoDeEmision

    def getLetra(self):
        return self.letra

    def getCliente(self):
        return self.cliente

    def getFechaDeEmision(self):
        return self.fechaDeEmision
