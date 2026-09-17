def calcular_costo_total(ruta, cantidad, descuento):
    try:
        precio_base = 50
        costo = (precio_base * cantidad) - descuento
        return costo
    except ValueError:
        print("Error de valor en el cálculo del costo.")
        return 0
    except Exception:
        print("Ocurrió un error inesperado en el cálculo del costo.")
        return 0
    finally:
        print("Finalizó el cálculo del costo total.")
def mostrar_resumen_reserva(ruta, cantidad, tipo, costo_total):
    print("-- RESUMEN DE RESERVA --")
    print(f"Ruta : {ruta}")
    print(f"Cantidad de pasajeros: {cantidad}")
    print(f"Tipo de pasajeros: {tipo}")
    print(f"Costo total: {costo_total}")

def validar_opciones(ruta, cantidad, tipo, costo_total):
    pass
