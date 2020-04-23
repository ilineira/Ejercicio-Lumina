from src.entidades.categoriasDeIVA.CategoriaDeIVA import CategoriaDeIVA


class CategoriaDeIVAResponsableInscripto(CategoriaDeIVA):

    codigo = 1
    descripcion = 'IVA Responsable Inscripto'
    letra = 'A'
    porcentaje = 10.05

    def getCodigo(self):
        return self.codigo

    def getLetra(self):
        return self.letra

    def getDescripcion(self):
        return self.descripcion

    def getPorcentaje(self):
        return self.porcentaje
