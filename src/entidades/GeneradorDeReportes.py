import datetime


class GeneradorDeReportes:

    def __init__(self, sistema):
        self.sistema = sistema

    def generarReporte(self, cosasPorProcesar):
        with open('sistema/Salida-{}.txt'.format(datetime.datetime.now().date())) as archivo:
            for cosa in cosasPorProcesar:
                archivo.write(cosa.generarReporte())
        self.sistema.reporteTerminado(cosasPorProcesar)