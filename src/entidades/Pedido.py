from src.entidades.estados.EstadoPendiente import EstadoPendiente
from src.entidades.factura.Factura import Factura


class Pedido:

    def __init__(self, codigo, cliente):
        self.producto = ''
        self.cantidadDeProducto = 0
        self.codigo = codigo
        self.cliente = cliente
        self.estado = EstadoPendiente()

    def getCodigo(self):
        return self.codigo

    def getCliente(self):
        return self.cliente

    def agregarProducto(self, producto, cantidad):
        self.producto = producto
        self.cantidadDeProducto = cantidad

    def facturar(self, numeroDeFactura):
        self.estado.facturar(self)
        return self.armarFactura(numeroDeFactura)

    def armarFactura(self, numeroDeFactura):
        factura = Factura(self, numeroDeFactura)
        return factura

    def getProducto(self):
        return self.producto

    def getCantidadDeProducto(self):
        return self.cantidadDeProducto

    def getEstado(self):
        return self.estado
