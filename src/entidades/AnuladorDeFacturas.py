class AnuladorDeFacturas:

    def __init__(self, sistema):
        self.sistema = sistema

    def anularFacturas(self, facturasAAnular):
        notasDeCredito = []
        for factura in facturasAAnular:
            factura.anular()
        self.sistema.anulacionTerminada(notasDeCredito)