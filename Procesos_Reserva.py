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
#el pass en esta parte del codigo es ocupada para rellenar y de iguial forma valide la sintaxis.
def mostrar_resumen_reserva(ruta, cantidad, tipo, costo_total):
    pass

def validar_opciones(ruta, cantidad, tipo, costo_total):
    pass
