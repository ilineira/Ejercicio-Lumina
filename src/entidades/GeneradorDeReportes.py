import datetime


class GeneradorDeReportes:

    def __init__(self, sistema):
        self.sistema = sistema

    def generarReporte(self, cosasPorProcesar):
        with open('/Users/ilineira/PycharmProjects/Ejercicio-Lumina/salidas/Salida-{}.txt'.format(datetime.datetime.now().date()), 'w') as archivo:
            for cosa in cosasPorProcesar:
                archivo.write(cosa.generarReporte())
        self.sistema.reporteTerminado(cosasPorProcesar)
