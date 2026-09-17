from seleccionar_ruta import seleccionar_ruta, ingresar_cantidad_pasajeros
from tipo_descuento import determinar_tipo_pasajero
from costo_resumen import finalizar_reserva

if __name__ == "__main__":
    print("=== Gestión de reservas - Empresa de transporte ===")
    ruta, precio = seleccionar_ruta()
    cantidad = ingresar_cantidad_pasajeros()
    tipo, porcentaje = determinar_tipo_pasajero()
    finalizar_reserva(ruta, precio, cantidad, tipo, porcentaje)
