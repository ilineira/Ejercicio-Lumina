class AnuladorDeFacturas:

    def __init__(self, sistema):
        self.sistema = sistema

    def anularFacturas(self, facturasAAnular):
        notasDeCredito = []
        for factura in facturasAAnular:

            self.sistema.factura.anular()
        return notasDeCredito