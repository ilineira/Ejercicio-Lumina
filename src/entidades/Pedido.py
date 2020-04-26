from src.entidades.estadosDePedido.EstadoPendiente import EstadoPendiente


class Pedido:

    def __init__(self, codigo, cliente):
        self.detalle = []
        self.codigo = codigo
        self.cliente = cliente
        self.estado = EstadoPendiente()

    def getCodigo(self):
        return self.codigo

    def getCliente(self):
        return self.cliente

    def agregarProducto(self, producto, cantidad):
        self.detalle.append([producto, cantidad])

    def getDetalle(self):
        return self.detalle
