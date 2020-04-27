from src.entidades.patrones.Singleton import Singleton
from src.entidades.GeneradorDeReportes import GeneradorDeReportes
from entidades.Facturador import Facturador
from src.entidades.AnuladorDeFacturas import AnuladorDeFacturas
from src.entidades.factura.Factura import Factura
import datetime
import schedule


class Sistema(Singleton):

    def __init__(self):
        self.notasDeCredito = []
        self.facturas = []
        self.porProcesar = []
        self.pedidosAFacturar = []
        self.pararProceso = False
        self.ultimoNumeroDeFactura = 1
        self.generadorDeReportes = GeneradorDeReportes(self)
        self.facturador = Facturador(self)
        self.anuladorDeFacturas = AnuladorDeFacturas(self)

    def arrancar(self):
        print('Sistema comenzo')
        self.pararProceso = False
        """schedule.every().day.at('20:00').do(self.facturar)
        while not self.pararProceso:
            schedule.run_pending()"""

    def parar(self):
        self.pararProceso = True
        print('Sistema parado')

    def facturar(self, pedidos):
        print('Facturando...')
        self.facturador.facturar(pedidos + self.pedidosAFacturar)
        self.generadorDeReportes.generarReporte(self.porProcesar)
        print('Finalizo facturacion')

    def anularFacturas(self, facturasAAnular):
        print('Cancelando pedidos...')
        self.anuladorDeFacturas.anularFacturas(facturasAAnular)

    def facturacionTerminada(self, facturas):
        self.porProcesar = facturas

    def reporteTerminado(self, cosasProcesadas):
        for cosa in cosasProcesadas:
            if cosa.__class__ == Factura:
                self.facturas.append(cosa)
            self.notasDeCredito.append(cosa)
        self.porProcesar.clear()

    def anulacionTerminada(self, notasDeCredito):
        self.porProcesar.append(notasDeCredito)

    def agregarPedidos(self, pedido):
        self.pedidosAFacturar.append(pedido)

    def getUltimoNumerodeFactura(self):
        numero = self.ultimoNumeroDeFactura
        self.ultimoNumeroDeFactura = self.ultimoNumeroDeFactura + 1
        return numero

    def eliminarPedido(self, pedido):
        try:
            self.pedidosAFacturar.remove(pedido)
        except:
            print('No existe ese pedido')

    def getFacturas(self):
        return self.facturas
