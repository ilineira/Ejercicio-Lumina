class AnuladorDeFacturas:

    def __init__(self, sistema):
        self.sistema = sistema

    def anularFacturas(self, facturasAAnular):
        notasDeCredito = []
        facturasEnSistema = self.sistema.getFacturas()
        for factura in facturasAAnular:
            if factura in facturasEnSistema:
                notasDeCredito.append(factura.anular())
        self.sistema.anulacionTerminada(notasDeCredito)
