
import threading


class CategoriaDeIVA:

    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance

    def getCodigo(self):
        return self.codigo


    def getDescripcion(self):
        return self.descripcion


    def getLetra(self):
        return self.letra

    def getPorcentaje(self):
        return self.porcentaje