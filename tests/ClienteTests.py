from src.entidades.Cliente import Cliente
import unittest


class ClienteTests(unittest.TestCase):

    def setUp(self) -> None:
        self.numeroDeCliente = 1
        self.domicilio = '9 de Julio'
        self.condicionImpositiva = 'Responsable inscripto'
        self.tipoDeDocumentoDNI = 'Dni'
        self.tipoDeDocumentoCUIT = 'Cuit'
        self.numeroDeDocumento = 123456789
        self.clienteConDNI = Cliente(self.numeroDeCliente, self.domicilio, self.condicionImpositiva, self.tipoDeDocumentoDNI, self.numeroDeDocumento)
        self.clienteConCuit = Cliente(self.numeroDeCliente, self.domicilio, self.condicionImpositiva, self.tipoDeDocumentoCUIT, self.numeroDeDocumento)

    def test01CreoClienteYVerificoNumeroDeCliente(self):
        self.assertEqual(self.clienteConDNI.getNumeroDeCliente(), self.numeroDeCliente)

    def test02CreoClienteYVerificoDomicilio(self):
        self.assertEqual(self.clienteConDNI.getDomicilio(), self.domicilio)

    def test03CreoClienteYVerificoNumeroDeDocumento(self):
        self.assertEqual(self.clienteConDNI.getNumeroDeDocumento(), self.numeroDeDocumento)

    def test04CreoClienteConDNIYVerificoTipoDeDocumento(self):
        self.assertEqual(self.clienteConDNI.getTipoDeDocumento(), self.tipoDeDocumentoDNI)

    def test05CreoClienteConCUITYVerificoTipoDeDocumento(self):
        self.assertEqual(self.clienteConCuit.getTipoDeDocumento(), self.tipoDeDocumentoCUIT)

    def test06CreoClienteConDNIYVerificoCondicionImpositiva(self):
        self.assertEqual(self.clienteConDNI.getCondicionImpositiva(), self.condicionImpositiva)



if __name__ == '__main__':
    unittest.main()
