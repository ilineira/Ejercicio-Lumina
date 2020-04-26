from src.entidades.estadosDePedido.EstadoPendiente import EstadoPendiente
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

    def getDetalle(self):
        return self.detalle

    def facturar(self):
        self.estado.facturar(self)
        return self.armarFactura()

    def armarFactura(self):
        factura = Factura(self)
        return factura

    def getProducto(self):
        return self.producto

    def getCantidadDeProducto(self):
        return self.cantidadDeProducto
