class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, n):
        self.stack.append(n)
        
    def pop(self):
        if len(self.stack) == 0:
            return 'Pila vacia'
        else:
            return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            return 'Pila vacia'
        else:
            return self.stack[-1]
    
s = Stack()
s.push(4)
s.push(3)
s.push(1)
s.push(6)
s.push(9)
print(s.stack)

def imprimir(s):
    s_aux = Stack()
    
    for _ in range(len(s.stack)):
        elemento = s.pop()
        print(elemento)
        print(s.stack)
        s_aux.push(elemento)
    
    for _ in range(len(s_aux.stack)):
        s.push(s_aux.pop())
        
    print(s.stack)

imprimir(s)