import datetime


class Cabecera:

    def __init__(self):
        self.fechaDeEmision = datetime.datetime.now().date()
        self.numeroDeFactura = ''
        self.codigoDeEmision = ''
        self.letra = ''
        self.cliente = ''

    def getCodigoDeEmision(self):
        return self.codigoDeEmision

    def getLetra(self):
        return self.letra

    def getCliente(self):
        return self.cliente
