class Pie:

    def __init__(self, detalle):
        self.total = detalle.getPrecioNETO()
        self.totalIVA = self.calcularTotalIVA(detalle)

    def calcularTotalIVA(self, detalle):
        return self.total + detalle.getMontoDeIVA()

    def getMonto(self):
        return self.total
