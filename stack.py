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
        return self.stack[-1]
    
s = Stack()
print(len(s.stack))
s.push(4)
print(s.stack)
s.push(3)
print(s.stack)
s.push(1)
print(s.stack)
s.push(6)
print(s.stack)
s.push(9)
print(s.stack)

print(s.pop())
print(s.stack)
print(s.pop())
print(s.stack)
print(s.pop())
print(s.stack)
print(s.pop())
print(s.stack)
print(s.pop())
print(s.stack)
print(s.pop())
print(s.stack)


