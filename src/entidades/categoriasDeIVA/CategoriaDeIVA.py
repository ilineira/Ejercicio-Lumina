from src.entidades.patrones.Singleton import Singleton
import threading


class CategoriaDeIVA(Singleton):

    def getCodigo(self):
        return self.instance().codigo

    def getDescripcion(self):
        return self.instance().descripcion

    def getLetra(self):
        return self.instance().letra

    def getPorcentaje(self):
        return self.instance().porcentaje
