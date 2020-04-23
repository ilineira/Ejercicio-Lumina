from src.entidades.categoriasDeIVA.CategoriaDeIVA import CategoriaDeIVA


class CategoriaDeIVANoResponsable(CategoriaDeIVA):
    codigo = 3
    descripcion = 'IVA no Responsable'
    letra = 'X'
    porcentaje = 71

    def getCodigo(self):
        return self.codigo

    def getLetra(self):
        return self.letra

    def getDescripcion(self):
        return self.descripcion

    def getPorcentaje(self):
        return self.porcentaje
