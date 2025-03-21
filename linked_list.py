class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
node1 = Node(10)
node2 = Node(1)
node3 = Node(100)
node4 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4


def imprimir(node):
    if node == None:
        return
    
    print(node.value)
    return imprimir(node.next)
    
    
imprimir(node1)
print('-------------')


def agregar(node, num):
    if node.next == None:
        node.next = Node(num)
        return
    return agregar(node.next, num)


agregar(node1, 999)
imprimir(node1)
print('-------------')


def contador(node, cuenta = 0):
    if node == None:
        return cuenta
    return contador(node.next, cuenta + 1)

print(contador(node1))
print('-------------')


def eliminar(node):
    if node.next.next == None:
        node.next = None
        return
    return eliminar(node.next)

eliminar(node1)
imprimir(node1)
    