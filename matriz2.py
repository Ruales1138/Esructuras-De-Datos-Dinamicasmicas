import random

def generar_matriz_recursivo(n: int, i: int = 0, j: int = 0, fila: list = [], matriz: list = []) -> list[list[int]]:
  if(i == n):
    return matriz
  if(j == n):
    matriz.append(fila)
    return generar_matriz_recursivo(n, i+1, 0, [], matriz)

  fila.append(random.randint(1,100))
  return generar_matriz_recursivo(n, i, j+1,fila, matriz)

# print(generar_matriz_recursivo(6, fila = [], matriz = []))


m = generar_matriz_recursivo(5, fila = [], matriz = [])
m


def encontrar_elemento_en_matriz(matriz: list[list[int]], elemento: int, fila: int = 0, columna: int = 0, numeros: list[int] = []) -> tuple[int, int]:

    if(fila == len(matriz)):
        return numeros
  
    if(columna == len(matriz)):
        return encontrar_elemento_en_matriz(matriz, elemento, fila+1, 0)
  
    if fila == 0:
        numeros.append(matriz[fila][columna])
    if fila == 4:
        numeros.append(matriz[fila][columna])
       

    return encontrar_elemento_en_matriz(matriz, elemento, fila, columna+1)

print(m)
print(encontrar_elemento_en_matriz(m, 59))