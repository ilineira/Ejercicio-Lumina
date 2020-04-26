from src.entidades.patrones.Singleton import Singleton


class Estado():

    def facturar(self):
        return self

    def getEstado(self):
        return self.estado
