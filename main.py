def main():
    try:
        ruta = seleccionar_ruta()
        cantidad = ingresar_cantidad_pasajeros()

        tipo = determinar_tipo_pasajero()
        descuento = calcular_descuento(tipo)

        costo_total = calcular_costo_total(ruta, cantidad, descuento)
        mostrar_resumen_reserva(ruta, cantidad, tipo, costo_total)
        validar_opciones(ruta, cantidad, tipo, costo_total)
#execpt y finally se utilizan para que dentro del try para poder campturar errores y que ciertas acciones o tareas se complten correctamente.
    except ValueError:
        print("Error de valor en los datos ingresados.")
    except Exception:
        print("Ocurrió un error inesperado.")
    finally:
        print("Proceso de reserva finalizado.")

if __name__ == "__main__":
    main()
