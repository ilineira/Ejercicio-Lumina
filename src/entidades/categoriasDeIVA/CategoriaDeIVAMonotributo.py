from src.entidades.categoriasDeIVA.CategoriaDeIVA import CategoriaDeIVA


class CategoriaDeIVAMonotributo(CategoriaDeIVA):
    codigo = 2
    descripcion = 'Monotributo'
    letra = 'B'
    porcentaje = 21

    def getCodigo(self):
        return self.codigo

    def getLetra(self):
        return self.letra

    def getDescripcion(self):
        return self.descripcion

    def getPorcentaje(self):
        return self.porcentaje
