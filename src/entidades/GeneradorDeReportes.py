import datetime


class GeneradorDeReportes:

    def generarReporte(self, facturas, notasDeCredito):
        with open('sistema/Salida-{}.txt'.format(datetime.datetime.now().date())) as archivo:
            for factura in facturas:

                archivo.write(factura.generarReporte())
            for notaDeCredito in notasDeCredito:
                archivo.write(notaDeCredito.generarReporte())
