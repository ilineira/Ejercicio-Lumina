from src.entidades.patrones.Singleton import Singleton
import threading
import schedule


class Sistema(Singleton):

    clientes = []
    facturas = []
    pedidos = []
    notasDeCredito = []
    pararProceso = False

    def arrancarSistema(self):
        self.pararProceso = False
        schedule.every().day.at('20:00').do(self.facturar)
        while not self.pararProceso:
            schedule.run_pending()

    def pararSistema(self):
        self.pararProceso = True

    def facturar(self):
        print('Facturando...')
