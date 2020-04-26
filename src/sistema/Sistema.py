from src.entidades.patrones.Singleton import Singleton
from src.entidades.GeneradorDeReportes import GeneradorDeReportes
from src.entidades.Facturador import Facturador
import schedule


class Sistema(Singleton):

    def __init__(self):

        self.clientes = []
        self.facturasYaFacturadas = []
        self.facturasPorFacturar = []
        self.notasDeCredito = []
        self.pararProceso = False
        self.generadorDeReportes = GeneradorDeReportes(self.instance())
        self.facturador = Facturador(self.instance())

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
        self.facturasYaFacturadas.append(self.facturador.facturar(self.facturasPorFacturar))
        self.generadorDeReportes.generarReporte(self.facturasYaFacturadas, self.notasDeCredito)
        print('Finalizo facturacion')

    def cancelarPedidos(self):
        print('Cancelando pedidos...')

    def facturacionTerminada(self):
        self.facturasPorFacturar.clear()
