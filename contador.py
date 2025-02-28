x = [1,2,43,5,66,77,87,5]

def contador(lista: list[int], idx: int = 0) -> int:
    if(idx == len(lista)):
        return idx
    else:
        return contador(lista, idx+1)
    

print(contador(x))