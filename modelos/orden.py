from modelos.menu import Bebida, PlatoPrincipal

class Orden:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        hay_plato = any(isinstance(i, PlatoPrincipal) for i in self.items)
        total = 0
        for i in self.items:
            if isinstance(i, Bebida):
                total += i.calcular_precio(descuento=hay_plato)
            else:
                total += i.calcular_precio()
        return round(total, 2)

    def mostrar(self):
        print("Resumen de la orden:")
        for item in self.items:
            print(item)
        print(f"Total: ${self.calcular_total()}")