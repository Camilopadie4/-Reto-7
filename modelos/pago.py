class MedioPago:
    def pagar(self, monto):
        raise NotImplementedError()

class Efectivo(MedioPago):
    def __init__(self, entregado):
        self.entregado = entregado

    def pagar(self, monto):
        if self.entregado >= monto:
            print(f"Pago en efectivo: ${monto} - Cambio: ${round(self.entregado - monto, 2)}")
        else:
            print(f"Faltan ${round(monto - self.entregado, 2)} para completar el pago.")

class Tarjeta(MedioPago):
    def __init__(self, numero):
        self.numero = numero

    def pagar(self, monto):
        print(f"Pago de ${monto} con tarjeta terminada en {self.numero[-4:]}")

class Pago:
    def __init__(self, orden, metodo: MedioPago):
        self.orden = orden
        self.metodo = metodo

    def procesar(self):
        total = self.orden.calcular_total()
        print("Procesando pago...")
        self.metodo.pagar(total)