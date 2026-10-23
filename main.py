# Archivo principal: main.py
# Proyecto: Conversor de Sistemas Numéricos (Universidad)

from conversiones import (
    decimal_a_binario, binario_a_decimal,
    decimal_a_octal, octal_a_decimal,
    decimal_a_hexadecimal, hexadecimal_a_decimal
)
from historial import agregar_historial, mostrar_historial
from practica import iniciar_practica

def validar_entrada(base):
    """Valida que la entrada cumpla con los caracteres permitidos según la base."""
    while True:
        entrada = input("Número a convertir (o escriba 'volver' para regresar): ").strip()
        if entrada.lower() == 'volver':
            return None
        if not entrada:
            print("Error: La entrada no puede estar vacía. Intente de nuevo.")
            continue
        
        valido = True
        if base == "Binario":
            for c in entrada:
                if c not in "01":
                    valido = False
                    break
        elif base == "Octal":
            for c in entrada:
                if c not in "01234567":
                    valido = False
                    break
        elif base == "Decimal":
            for c in entrada:
                if c not in "0123456789":
                    valido = False
                    break
        elif base == "Hexadecimal":
            for c in entrada:
                if c not in "0123456789ABCDEFabcdef":
                    valido = False
                    break
        
        if not valido:
            print(f"Error: Caracteres inválidos para el sistema {base}. Intente de nuevo.")
        else:
            return entrada

def seleccionar_base(tipo):
    """Muestra el submenú para elegir la base de origen o destino."""
    while True:
        print(f"\nSELECCIONE LA BASE DE {tipo}")
        print("1. Binario")
        print("2. Octal")
        print("3. Decimal")
        print("4. Hexadecimal")
        print("6. Volver al menú principal" if tipo == "ORIGEN" else "0. Volver al menú principal")
        
        op = input("Seleccione una opción: ").strip()
        
        if tipo == "ORIGEN" and op == "6": return None
        if tipo == "DESTINO" and op == "0": return None
        
        bases_map = {"1": "Binario", "2": "Octal", "3": "Decimal", "4": "Hexadecimal"}
        if op in bases_map:
            return bases_map[op]
        print("Opción inválida. Intente de nuevo.")

def realizar_conversion(historial):
    """Gestiona el flujo completo de una conversión entre bases."""
    base_origen = seleccionar_base("ORIGEN")
    if not base_origen: return
    
    base_destino = seleccionar_base("DESTINO")
    if not base_destino: return
    
    if base_origen == base_destino:
        print("\nError: La base de origen y destino no pueden ser iguales.")
        input("Presione Enter para continuar...")
        return

    print(f"\nCONVERSIÓN: {base_origen.upper()} A {base_destino.upper()}")
    print("Ingrese un entero no negativo de hasta 128 dígitos.")
    
    valor_str = validar_entrada(base_origen)
    if not valor_str: return

    # 1. Convertir origen a decimal
    if base_origen == "Binario":
        dec = binario_a_decimal(valor_str)
    elif base_origen == "Octal":
        dec = octal_a_decimal(valor_str)
    elif base_origen == "Decimal":
        dec = int(valor_str)
    elif base_origen == "Hexadecimal":
        dec = hexadecimal_a_decimal(valor_str)

    # 2. Convertir decimal a destino
    if base_destino == "Binario":
        resultado = decimal_a_binario(str(dec))
    elif base_destino == "Octal":
        resultado = decimal_a_octal(str(dec))
    elif base_destino == "Decimal":
        resultado = str(dec)
    elif base_destino == "Hexadecimal":
        resultado = decimal_a_hexadecimal(str(dec))

    # Mostrar resultados
    print("\n" + "=" * 40)
    print("RESULTADO")
    print("=" * 40)
    print(f"Número ingresado: {valor_str}")
    print(f"Base de origen: {base_origen}")
    print(f"Base de destino: {base_destino}")
    print(f"Resultado: {resultado}")
    print("=" * 40)

    # Registrar en el historial
    operacion = {
        "entrada": valor_str,
        "origen": base_origen,
        "destino": base_destino,
        "resultado": resultado
    }
    agregar_historial(historial, operacion)
    print("Conversión agregada al historial.")
    input("\nPresione Enter para continuar...")

def mostrar_menu():
    """Muestra el menú principal en la consola."""
    print("\n" + "=" * 60)
    print("CONVERSOR DE SISTEMAS NUMÉRICOS")
    print("=" * 60)
    print("1. Realizar una conversión")
    print("2. Consultar el historial")
    print("3. Iniciar el modo de práctica")
    print("4. Salir")
    print("=" * 60)

def main():
    """Función principal que controla el flujo del programa."""
    historial = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            realizar_conversion(historial)
        elif opcion == "2":
            mostrar_historial(historial)
        elif opcion == "3":
            iniciar_practica()
        elif opcion == "4":
            print("\n¡Gracias por utilizar el conversor! Saliendo del programa...")
            break
        else:
            print("\nOpción inválida. Por favor, seleccione un número entre 1 y 4.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()