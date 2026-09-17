from tipo_Descuento import calcular_descuentos
def validar_opciones(ruta, precio, cantidad, tipo):
    try:
        if ruta == "" or precio <= 0:
            print("La ruta no es válida.")
            return False
        if cantidad <= 0:
            print("La cantidad de pasajeros no es válida.")
            return False
        if tipo == "":
            print("El tipo de pasajero no es válido.")
            return False
        return True
    except:
        print("Error al validar las opciones.")
        return False
    finally:
        print("Validación terminada.")
def calcular_costo_total(precio, cantidad, descuento_total):
    subtotal = precio * cantidad
    total = subtotal - descuento_total
    return subtotal, total
def mostrar_resumen(ruta, precio, cantidad, tipo, porcentaje, descuento_boleto, descuento_total, subtotal, total):
    print("\n========== RESUMEN DE LA RESERVA ==========")
    print("Ruta:", ruta)
    print("Precio por boleto: $", precio)
    print("Cantidad de pasajeros:", cantidad)
    print("Tipo de pasajero:", tipo)
    print("Descuento aplicado:", porcentaje, "%")
    print("Descuento por boleto: $", descuento_boleto)
    print("Descuento total: $", descuento_total)
    print("Subtotal: $", subtotal)
    print("Costo total a pagar: $", total)
    print("===========================================\n")
def finalizar_reserva(ruta, precio, cantidad, tipo, porcentaje):
    if validar_opciones(ruta, precio, cantidad, tipo) == False:
        print("No se puede continuar con la reserva.")
        return
    descuento_boleto, descuento_total = calcular_descuentos(precio, cantidad, porcentaje)
    subtotal, total = calcular_costo_total(precio, cantidad, descuento_total)
    mostrar_resumen(ruta, precio, cantidad, tipo, porcentaje, descuento_boleto, descuento_total, subtotal, total)