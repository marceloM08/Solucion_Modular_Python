from rutas import chooseRoutes, insertpassengerAmount
from tipo_Descuento import determinar_tipo_pasajero
from costo_resumen import finalizar_reserva

if __name__ == "__main__":
    print("=== Gestión de reservas - Empresa de transporte ===")
    ruta, precio = chooseRoutes()
    cantidad = insertpassengerAmount()
    tipo, porcentaje = determinar_tipo_pasajero()
    finalizar_reserva(ruta, precio, cantidad, tipo, porcentaje)
