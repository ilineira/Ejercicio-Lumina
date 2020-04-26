from src.entidades.estadosDePedido.Estado import Estado
from src.entidades.estadosDePedido.EstadoFacturado import EstadoFacturado


class EstadoPendiente(Estado):

    estado = 'Pendiente'

    def facturar(self, pedido):
        return EstadoFacturado()
