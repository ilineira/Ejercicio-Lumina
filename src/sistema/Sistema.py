from src.entidades.patrones.Singleton import Singleton
from src.entidades.GeneradorDeReportes import GeneradorDeReportes
from src.entidades.Facturador import Facturador
import schedule


class Sistema(Singleton):

    def __init__(self):

        self.clientes = []
        self.facturas = []
        self.pedidos = []
        self.notasDeCredito = []
        self.pararProceso = False
        self.generadorDeReportes = GeneradorDeReportes()
        self.facturador = Facturador()

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
        self.facturador.facturar(self.pedidos)
        self.generadorDeReportes.generarReporte(self.facturas, self.notasDeCredito)
        print('Finalizo facturacion')
