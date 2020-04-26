from src.entidades.patrones.Singleton import Singleton
from src.entidades.GeneradorDeReportes import GeneradorDeReportes
from src.entidades.Facturador import Facturador
from src.entidades.AnuladorDeFacturas import AnuladorDeFacturas
import datetime
import schedule


class Sistema(Singleton):

    def __init__(self):
        self.procesados = {}
        self.facturas = []
        self.porProcesar = []
        self.pedidosPorFacturar = []
        self.pararProceso = False
        self.generadorDeReportes = GeneradorDeReportes(self.instance())
        self.facturador = Facturador(self.instance())
        self.anuladorDeFacturas = AnuladorDeFacturas(self.instance())

    def arrancarSistema(self):
        print('Sistema comenzo')
        self.pararProceso = False
        schedule.every().day.at('20:00').do(self.facturar)
        while not self.pararProceso:
            schedule.run_pending()

    def pararSistema(self):
        self.pararProceso = True
        print('Sistema parado')

    def facturar(self):
        print('Facturando...')
        self.facturador.facturar(self.pedidosPorFacturar)
        self.generadorDeReportes.generarReporte(self.porProcesar)

        print('Finalizo facturacion')

    def anularFacturas(self, facturasAAnular):
        print('Cancelando pedidos...')
        self.porProcesar.append(self.anuladorDeFacturas.anularFacturas(facturasAAnular))

    def facturacionTerminada(self, facturas):
        self.porProcesar.append(facturas)
        self.pedidosPorFacturar.clear()

    def reporteTerminado(self, cosasProcesadas):
        self.procesados[datetime.datetime.now().date()] = cosasProcesadas
        self.porProcesar.clear()
        self.facturas.clear()

    def cargarPedido(self, pedido):
        self.pedidosPorFacturar.append(pedido)
        return 'Pedido cargado'


