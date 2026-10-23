# Módulo: conversiones.py
# Contiene la lógica matemática manual para las conversiones entre bases.

def decimal_a_binario(numero_str):
    num = int(numero_str)
    if num == 0:
        return "0"
    binario = ""
    while num > 0:
        residuo = num % 2
        binario = str(residuo) + binario
        num = num // 2
    return binario

def binario_a_decimal(numero_str):
    decimal = 0
    potencia = 0
    for digito in reversed(numero_str):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1
    return decimal

def decimal_a_octal(numero_str):
    num = int(numero_str)
    if num == 0:
        return "0"
    octal = ""
    while num > 0:
        residuo = num % 8
        octal = str(residuo) + octal
        num = num // 8
    return octal

def octal_a_decimal(numero_str):
    decimal = 0
    potencia = 0
    for digito in reversed(numero_str):
        decimal += int(digito) * (8 ** potencia)
        potencia += 1
    return decimal

def decimal_a_hexadecimal(numero_str):
    num = int(numero_str)
    if num == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while num > 0:
        residuo = num % 16
        hexadecimal = hex_chars[residuo] + hexadecimal
        num = num // 16
    return hexadecimal

def hexadecimal_a_decimal(numero_str):
    hex_chars = "0123456789ABCDEF"
    decimal = 0
    potencia = 0
    for digito in reversed(numero_str.upper()):
        valor = hex_chars.index(digito)
        decimal += valor * (16 ** potencia)
        potencia += 1
    return decimal