# Módulo: practica.py
# Gestiona el modo de práctica con ejercicios aleatorios.

import random
from conversiones import (
    decimal_a_binario, binario_a_decimal,
    decimal_a_octal, octal_a_decimal,
    decimal_a_hexadecimal, hexadecimal_a_decimal
)

def convertir_general(valor_str, base_origen, base_destino):
    """Realiza la conversión entre cualquier par de bases usando decimal como intermediario."""
    # 1. Convertir origen a decimal
    if base_origen == "Binario":
        dec = binario_a_decimal(valor_str)
    elif base_origen == "Octal":
        dec = octal_a_decimal(valor_str)
    elif base_origen == "Decimal":
        dec = int(valor_str)
    elif base_origen == "Hexadecimal":
        dec = hexadecimal_a_decimal(valor_str)
    else:
        return None

    # 2. Convertir decimal a destino
    if base_destino == "Binario":
        return decimal_a_binario(str(dec))
    elif base_destino == "Octal":
        return decimal_a_octal(str(dec))
    elif base_destino == "Decimal":
        return str(dec)
    elif base_destino == "Hexadecimal":
        return decimal_a_hexadecimal(str(dec))
    else:
        return None

def iniciar_practica():
    """Controla el flujo del modo de práctica."""
    aciertos = 0
    respondidos = 0
    bases = ["Binario", "Octal", "Decimal", "Hexadecimal"]

    while True:
        print("\n" + "=" * 60)
        print("MODO DE PRÁCTICA")
        print("=" * 60)
        porcentaje = (aciertos / respondidos * 100) if respondidos > 0 else 0.0
        print(f"Aciertos: {aciertos}")
        print(f"Ejercicios respondidos: {respondidos}")
        print(f"Porcentaje de aciertos: {porcentaje:.1f}%")
        print("=" * 60)
        print("1. Resolver un nuevo ejercicio")
        print("2. Reiniciar puntuación")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            num_dec = random.randint(0, 255)
            b_origen, b_destino = random.sample(bases, 2)
            
            if b_origen == "Binario":
                val_orig = decimal_a_binario(str(num_dec))
            elif b_origen == "Octal":
                val_orig = decimal_a_octal(str(num_dec))
            elif b_origen == "Decimal":
                val_orig = str(num_dec)
            elif b_origen == "Hexadecimal":
                val_orig = decimal_a_hexadecimal(str(num_dec))

            respuesta_correcta = convertir_general(val_orig, b_origen, b_destino)

            print("\n" + "=" * 60)
            print("EJERCICIO DE PRÁCTICA")
            print("=" * 60)
            print(f"Convierta {val_orig} de {b_origen} a {b_destino}.")
            print("\nIngrese únicamente el número de la respuesta.")
            
            respuesta_usuario = input("Su respuesta: ").strip().upper()
            
            respondidos += 1
            if respuesta_usuario == respuesta_correcta.upper():
                print("\n¡Respuesta correcta!")
                aciertos += 1
            else:
                print(f"\nRespuesta incorrecta. La respuesta esperada era: {respuesta_correcta}")
            
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            aciertos = 0
            respondidos = 0
            print("¡Puntuación reiniciada!")
            input("Presione Enter para continuar...")

        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")