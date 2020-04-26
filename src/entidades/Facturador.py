from queue import Queue
import threading


class Facturador:

    def __init__(self, sistema):
        self.sistema = sistema
        self.queue = Queue()
        self.cantidadDeHilos = 2
        self.hilos = []
        self.facturas = []
        self.blockear = threading.Lock

    def facturar(self, pedidos):
        [self.queue.put(pedido) for pedido in pedidos]

        for _ in range(self.cantidadDeHilos):
            hilo = threading.Thread(target=self.facturarPedido())
            hilo.start()

        for hilo in self.hilos:
            hilo.join()

        self.terminarFacturacion()

    def facturarPedido(self):
        while self.queue.not_empty:
            self.blockear.acquire()
            self.facturas.append(self.queue.get().facturar())
            self.blockear.release()

    def terminarFacturacion(self):
        self.sistema.facturacionTerminada(self.facturas)
