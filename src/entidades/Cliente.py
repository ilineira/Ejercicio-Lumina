from src.entidades.categoriasDeIVA.CategoriaDeIVAFactory import CategoriaDeIVAFactory


class Cliente(object):

    def __init__(self, numeroDeCliente, domicilio, condicionImpositiva, tipoDeDocumento, numeroDeDocumento):
        self.numeroDeCliente = numeroDeCliente
        self.domicilio = domicilio
        self.condicionImpositiva = CategoriaDeIVAFactory.getCategoriaDeIVA(condicionImpositiva)
        self.tipoDeDocumento = tipoDeDocumento
        self.numeroDeDocumento = numeroDeDocumento

    def getNumeroDeCliente(self):
        return self.numeroDeCliente

    def getDomicilio(self):
        return self.domicilio

    def getCondicionImpositiva(self):
        return self.condicionImpositiva

    def getTipoDeDocumento(self):
        return self.tipoDeDocumento

    def getNumeroDeDocumento(self):
        return self.numeroDeDocumento
