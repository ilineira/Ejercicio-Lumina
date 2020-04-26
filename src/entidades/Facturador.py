class Facturador:

    def __init__(self, sistema):
        self.sistema = sistema

    def facturar(self, pedidos):
        facturas = []
        for pedido in pedidos:
            facturas.append(pedido.facturar())
        self.sistema.facturacionTerminada(facturas)
