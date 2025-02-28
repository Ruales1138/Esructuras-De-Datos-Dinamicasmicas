numero1 = 12345
numero2 = 987654

def contar_digitos(numero, contador = 0):
    if numero == 0:
        return contador
    else:
        numero_nuevo  = numero // 10
        return contar_digitos(numero_nuevo, contador + 1)

print(contar_digitos(numero1))