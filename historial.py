# Módulo: historial.py
# Gestiona el almacenamiento, visualización y administración del historial.

def agregar_historial(historial, operacion):
    """Agrega una nueva operación al historial."""
    historial.append(operacion)

def mostrar_historial(historial):
    """Muestra el historial y permite eliminar o vaciar registros."""
    while True:
        print("\n" + "=" * 60)
        print("HISTORIAL DE CONVERSIONES")
        print("=" * 60)
        
        if not historial:
            print("Aún no hay conversiones registradas en esta sesión.")
            print("=" * 60)
            input("Presione Enter para regresar al menú principal...")
            break
        else:
            for i, item in enumerate(historial, 1):
                print(f"Registro {i}")
                print(f"  Entrada: {item['entrada']}")
                print(f"  Origen: {item['origen']}")
                print(f"  Destino: {item['destino']}")
                print(f"  Resultado: {item['resultado']}")
                print("-" * 40)
            
            print(f"Total de registros: {len(historial)}")
            print("=" * 60)
            print("1. Eliminar un registro")
            print("2. Vaciar historial")
            print("3. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                try:
                    num = int(input("Ingrese el número del registro a eliminar: "))
                    if 1 <= num <= len(historial):
                        historial.pop(num - 1)
                        print(f"¡Registro {num} eliminado con éxito!")
                        input("Presione Enter para continuar...")
                    else:
                        print("Error: El número de registro no existe.")
                        input("Presione Enter para continuar...")
                except ValueError:
                    print("Error: Debe ingresar un número válido.")
                    input("Presione Enter para continuar...")
            elif opcion == "2":
                confirmar = input("¿Está seguro de vaciar todo el historial? (s/n): ").strip().lower()
                if confirmar == 's':
                    historial.clear()
                    print("¡Historial vaciado correctamente!")
                    input("Presione Enter para continuar...")
                    break
            elif opcion == "3":
                break
            else:
                print("Opción inválida. Intente de nuevo.")
                input("Presione Enter para continuar...")