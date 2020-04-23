from abc import abstractmethod, ABCMeta
import threading


class CategoriaDeIVA(metaclass=ABCMeta):

    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance

    @abstractmethod
    def getCodigo(self):
        """Devuelve codigo de categoria de iva"""

    @abstractmethod
    def getDescripcion(self):
        """Devuelve descripcion de categoria de iva"""

    @abstractmethod
    def getLetra(self):
        """Devuelve letra de categoria de iva"""

    def getPorcentaje(self):
        """Devuelve porcentaje de categoria de iva"""