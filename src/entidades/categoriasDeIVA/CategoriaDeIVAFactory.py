from src.entidades.categoriasDeIVA.CategoriaDeIVAMonotributo import CategoriaDeIVAMonotributo
from src.entidades.categoriasDeIVA.CategoriaDeIVANoResponsable import CategoriaDeIVANoResponsable
from src.entidades.categoriasDeIVA.CategoriaDeIVAResponsableInscripto import CategoriaDeIVAResponsableInscripto


class CategoriaDeIVAFactory:

    categoriasDeIVA = {
        'Responsable Inscripto': CategoriaDeIVAResponsableInscripto,
        'Monotributo': CategoriaDeIVAMonotributo,
        'No Responsable': CategoriaDeIVANoResponsable
    }

    @classmethod
    def getCategoriaDeIVA(cls, tipoDeIVA):
        return cls.categoriasDeIVA[tipoDeIVA]().instance()
