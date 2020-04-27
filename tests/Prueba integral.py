from src.sistema.Sistema import Sistema
from src.entidades.Pedido import Pedido
from src.entidades.Cliente import Cliente
from src.entidades.Producto import Producto
import random

def crearClientes():
    clientes = [
        Cliente(1, '9 de julio', 'Responsable Inscripto', 'Dni', 1234),
        Cliente(2, '9 de julio', 'Monotributo', 'Dni', 1234),
        Cliente(3, '9 de julio', 'No Responsable', 'Dni', 1234),
        Cliente(4, '9 de julio', 'Responsable Inscripto', 'Cuit', 1234),
        Cliente(5, '9 de julio', 'Monotributo', 'Cuit', 1234),
        Cliente(6, '9 de julio', 'No Responsable', 'Cuit', 1234)
    ]
    return clientes


def armarPedidos():
    pedidos = []
    clientes = crearClientes()

    for i in range(5000):
        cliente = random.choice(clientes)
        producto = Producto(1, 'Producto1', random.randint(0,10))
        pedido = Pedido(random.randint(1,100), cliente)
        pedido.agregarProducto(producto, random.randint(1, 50))

        pedidos.append(pedido)

    return pedidos




def main():
    sistema = Sistema()
    print('Se instancio el sistema')
    sistema.arrancar()
    pedidos = armarPedidos()
    sistema.agregarPedidos(pedidos)

    sistema.facturar(pedidos)

    pedidos = armarPedidos()
    sistema.agregarPedidos(pedidos)

    facturas = sistema.getFacturas()
    facturasAEliminar = []
    for i in range(100):
        facturasAEliminar.append(random.choice(facturas))

    sistema.anularFacturas(facturasAEliminar)







    print('Comienzo a facturar')


    sistema.parar()
    return

if __name__ == '__main__':
    main()