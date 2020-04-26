class Detalle:

    def __init__(self, pedido):
        self.producto = pedido.getProducto()
        self.precioUnitario = self.producto.precio
        self.porcentajeDeIVA = pedido.getCliente().getCondicionImpositiva().getPorcentaje()
        self.cantidad = pedido.getCantidadDeProducto()
        self.precioNETO = self.calcularPrecioNETO()
        self.montoDeIVA = self.calcularMontoDeIVA()
        """Revisar documentacion, entidades a crear -> porcentajeDeIVA = montoDeIVA"""
        self.precioDeVenta = self.calcularPrecioDeVenta()

    def calcularPrecioNETO(self):
        return self.producto.getPrecio() * self.cantidad

    def calcularPrecioDeVenta(self):
        return self.precioNETO + self.montoDeIVA

    def calcularMontoDeIVA(self):
        return self.producto.getPrecio() * (self.porcentajeDeIVA / 100)

    def getPrecioNETO(self):
        return self.precioNETO

    def getMontoDeIVA(self):
        return self.montoDeIVA
