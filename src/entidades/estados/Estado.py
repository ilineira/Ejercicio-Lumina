from src.entidades.patrones.Singleton import Singleton


class Estado:

    def facturar(self, pedido):
        return self

    def getEstado(self):
        return self.estado
