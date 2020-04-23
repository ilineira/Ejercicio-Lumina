from src.entidades.categoriasDeIVA.CategoriaDeIVA import CategoriaDeIVA


class CategoriaDeIVANoResponsable(CategoriaDeIVA):
    codigo = 3
    descripcion = 'IVA no Responsable'
    letra = 'X'
    porcentaje = 71
