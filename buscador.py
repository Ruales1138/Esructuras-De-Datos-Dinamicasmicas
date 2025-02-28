x = [1,2,43,5,66,77,87,5]

def buscador(lista: list[int], numero: int, idx: int = 0) -> bool:
    if(idx == len(lista)):
        return False
    if(numero == lista[idx]):
        return True
    else:
        return buscador(lista, numero, idx+1)
    

print(buscador(x, 2))