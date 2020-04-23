from src.entidades.categoriasDeIVA.CategoriaDeIVAFactory import CategoriaDeIVAFactory
import unittest


class CategoriaDeIVATests(unittest.TestCase):

    def test01CategoriaDeIVAResponsableInscriptoEsSingleton(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('Responsable Inscripto')
        categoriaDeIVA2 = CategoriaDeIVAFactory.getCategoriaDeIVA('Responsable Inscripto')
        self.assertEqual(categoriaDeIVA1.__hash__(), categoriaDeIVA2.__hash__())

    def test02CategoriaDeIVAResponsableInscriptoVerificoCodigo(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('Responsable Inscripto')
        self.assertEqual(categoriaDeIVA1.getCodigo(), 1)

    def test03CategoriaDeIVAResponsableInscriptoVerificoLetra(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('Responsable Inscripto')
        self.assertEqual(categoriaDeIVA1.getLetra(), 'A')

    def test04CategoriaDeIVAResponsableInscriptoVerificoDescripcion(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('Responsable Inscripto')
        self.assertEqual(categoriaDeIVA1.getDescripcion(), 'IVA Responsable Inscripto')

    def test05CategoriaDeIVAResponsableInscriptoVerificoPorcentaje(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('Responsable Inscripto')
        self.assertEqual(categoriaDeIVA1.getPorcentaje(), 10.05)

    def test06CategoriaDeIVAMonotributoEsSingleton(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('Monotributo')
        categoriaDeIVA2 = CategoriaDeIVAFactory.getCategoriaDeIVA('Monotributo')
        self.assertEqual(categoriaDeIVA1.__hash__(), categoriaDeIVA2.__hash__())

    def test07CategoriaDeIVAMonotributoVerificoCodigo(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('Monotributo')
        self.assertEqual(categoriaDeIVA1.getCodigo(), 2)

    def test08CategoriaDeIVAMonotributoVerificoLetra(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('Monotributo')
        self.assertEqual(categoriaDeIVA1.getLetra(), 'B')

    def test09CategoriaDeIVAMonotributoVerificoDescripcion(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('Monotributo')
        self.assertEqual(categoriaDeIVA1.getDescripcion(), 'Monotributo')

    def test10CategoriaDeIVAMonotributoVerificoPorcentaje(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('Monotributo')
        self.assertEqual(categoriaDeIVA1.getPorcentaje(), 21)

    def test11CategoriaDeIVAMonotributoEsSingleton(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('No Responsable')
        categoriaDeIVA2 = CategoriaDeIVAFactory.getCategoriaDeIVA('No Responsable')
        self.assertEqual(categoriaDeIVA1.__hash__(), categoriaDeIVA2.__hash__())

    def test12CategoriaDeIVAMonotributoVerificoCodigo(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('No Responsable')
        self.assertEqual(categoriaDeIVA1.getCodigo(), 3)

    def test13CategoriaDeIVAMonotributoVerificoLetra(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('No Responsable')
        self.assertEqual(categoriaDeIVA1.getLetra(), 'X')

    def test14CategoriaDeIVAMonotributoVerificoDescripcion(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('No Responsable')
        self.assertEqual(categoriaDeIVA1.getDescripcion(), 'IVA no Responsable')

    def test15CategoriaDeIVAMonotributoVerificoPorcentaje(self):
        categoriaDeIVA1 = CategoriaDeIVAFactory.getCategoriaDeIVA('No Responsable')
        self.assertEqual(categoriaDeIVA1.getPorcentaje(), 71)
