from gestor_menu import GestorMenu
from modelos.menu import Bebida, PlatoPrincipal
from modelos.orden import Orden
from modelos.restaurante import Restaurante
from modelos.pago import Efectivo, Tarjeta, Pago

# Crear menú y agregar elementos
menu = GestorMenu()
menu.agregar_item("Agua", 2.0, "Bebida")
menu.agregar_item("Hamburguesa", 8.0, "PlatoPrincipal")
menu.mostrar_menu()

# Crear ítems
agua = Bebida("Agua", 2.0, "500ml")
hamburguesa = PlatoPrincipal("Hamburguesa", 8.0, "Grande")

# Crear orden
orden1 = Orden()
orden1.agregar_item(agua)
orden1.agregar_item(hamburguesa)

# Restaurante y flujo
restaurante = Restaurante()
restaurante.recibir_orden(orden1)

# Atender orden y pagar
orden_atendida = restaurante.atender_siguiente()
if orden_atendida:
    metodo_pago = Efectivo(15)  # Puedes probar también con Tarjeta("1234567890123456")
    pago = Pago(orden_atendida, metodo_pago)
    pago.procesar()