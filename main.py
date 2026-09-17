from rutas import chooseRoutes, insertpassengerAmount
from tipo_Descuento import detPassType
from costo_resumen import finalizar_reserva

if __name__ == "__main__":
    print("=== Gestión de reservas - Empresa de transporte ===")
    ruta, precio = chooseRoutes()
    cantidad = insertpassengerAmount()
    tipo, porcentaje = detPassType()
    finalizar_reserva(ruta, precio, cantidad, tipo, porcentaje)
