def calcular_costo_total(ruta, cantidad, descuento):
    try:
        precio_base = 100
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
