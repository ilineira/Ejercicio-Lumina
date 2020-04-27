from queue import Queue
import threading
import time


class Facturador:

    def __init__(self, sistema):
        self.sistema = sistema
        self.queue = Queue(maxsize=0)
        self.cantidadDeHilos = 2
        self.hilos = []
        self.facturas = []
        self.lock = threading.Lock()

    def facturar(self, pedidos):
        for i in range(self.cantidadDeHilos):
            hilo = threading.Thread(target=self.facturarPedido, args=(pedidos, ), daemon=True)
            hilo.start()
            self.hilos.append(hilo)

        for hilo in self.hilos:
            hilo.join()

        self.terminarFacturacion()

    def facturarPedido(self, pedidos):
        while len(pedidos) > 1:
            self.lock.acquire()
            try:
                pedido = pedidos.pop()
                self.facturas.append(pedido.facturar(self.sistema.getUltimoNumerodeFactura()))
            except:
                print('Error')
            finally:
                self.lock.release()


    def terminarFacturacion(self):
        self.sistema.facturacionTerminada(self.facturas)
