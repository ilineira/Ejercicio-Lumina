from src.entidades.estados.Estado import Estado
from src.entidades.estados.EstadoListoParaDespachar import EstadoListoParaDespachar


class EstadoPendiente(Estado):

    estado = 'Pendiente'

    def facturar(self, pedido):
        return EstadoListoParaDespachar()
