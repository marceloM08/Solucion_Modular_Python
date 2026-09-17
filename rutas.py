""" este archivo es donde estan guardados las funciones de las rutas"""
def chooseRoutes():
    print("=Rutas Disponibles/Trabajando=")
    print("1. Leon - Granada C$300 ")
    print("2. Managua - Esteli C$260 ")
    print("3. Masaya - San Juan del Sur C$499 ")
    print("4. Chinandega - Matagalpa C$200 ")
    print("5. Managua - Leon C$340 ")

    try:
        op = int(input("Seleccione una opcion del 1 al 5: "))
        if op == 1:
            return "Leon - Granada", 300
        elif op == 2:
            return "Managua - Esteli", 260
        elif op == 3:
            return "Masaya - San Juan del Sur", 499
        elif op == 4:
            return "Chinandega - Matagalpa", 200
        elif op == 5:
            return "Managua - Leon", 340
        else:
            print("Ruta no válida.")
            return chooseRoutes()
    except ValueError:
        print("Debe ingresar un número válido.")
        return chooseRoutes()

def insertpassengerAmount():
    try:
        amount = int(input("Ingrese la Cantidad de pasajeros: "))
        if amount <= 0:
            print("La cantidad ingresada debe ser mayor a 0")
            return insertpassengerAmount()
        return amount
    except ValueError:
        print("Debe ingresar un numero valido.")
        return insertpassengerAmount()
    
    

