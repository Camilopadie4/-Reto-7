class Menu:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio(self):
        return self.precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Bebida(Menu):
    def __init__(self, nombre, precio, tamaño):
        super().__init__(nombre, precio)
        self.tamaño = tamaño

    def calcular_precio(self, descuento=False):
        return self.precio * 0.85 if descuento else self.precio

    def __str__(self):
        return f"{self.nombre} ({self.tamaño}) - ${self.precio}"

class PlatoPrincipal(Menu):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio)
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} Porción: {self.cantidad} - ${self.precio}"