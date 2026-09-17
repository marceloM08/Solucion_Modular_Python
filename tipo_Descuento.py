def determinar_tipo_pasajero():
    print("Tipos de pasajero")
    print("1. Adulto  (0%)")
    print("2. Niño  (20%)")
    print("3. Estudiante  (15%)")
    print("4. Tercera edad  (25%)")
    try:
        opcion = input("Seleccione el tipo de pasajero (1-4): ")
        if opcion == "1":
            return "Adulto", 0
        elif opcion == "2":
            return "Niño", 20
        elif opcion == "3":
            return "Estudiante", 15
        elif opcion == "4":
            return "Tercera edad", 25
        else:
            print("Tipo no válido.")
            return determinar_tipo_pasajero()
    except:
        print("Error al elegir el tipo de pasajero.")
        return determinar_tipo_pasajero()
def calcular_descuentos(precio, cantidad, porcentaje):
    descuento_boleto = precio * porcentaje / 100
    descuento_total = descuento_boleto * cantidad
    return descuento_boleto, descuento_t