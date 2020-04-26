class Facturador:

    def facturar(self, pedidos):
        facturas = []
        for pedido in pedidos:
            facturas.append(pedido.facturar())
        return facturas
