class NotaDeCredito:

    def __init__(self, cliente, cabecera, pie):
        self.cliente = cliente
        self.cabecera = cabecera
        self.pie = pie

    def generarReporte(self):
        linea = '{0}-{1}-{2}-{3}-{4}-{5}'.format(self.cliente.getNumeroDeCliente(),
                                                 self.cliente.getTipoDeDocumento(),
                                                 self.cabecera.getLetra(),
                                                 self.cabecera.getCodigoDeEmision(),
                                                 self.cabecera.getFechaDeEmision(),
                                                 self.pie.getMonto())
        return linea