x = [1, 2, 3, 4, 5]
x2 = [10, -5, 7]

def sumar(lista: list[int], idx: int = 0) -> int:
    if(idx == len(lista)):
        return 0
    else:
        return lista[idx] + sumar(lista, idx+1)
    

print(sumar([]))