class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, n):
        self.queue.append(n)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def fist(self):
        return self.queue[0]
    
    def __repr__(self):
        return self.queue
    
    
q = Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(34)
q.enqueue(8)
q.enqueue(10)
print(q.queue)

    
def invertir_cola(cola):
    cola_aux = Queue()
    
    for _ in range((len(cola.queue))):
        elemento = cola.dequeue()
        print(elemento)
        print(cola.queue)
        cola_aux.enqueue(elemento)
        
    for _ in range(len(cola_aux.queue)):
        cola.enqueue(cola_aux.dequeue())
        
    return cola.queue


print(invertir_cola(q))

for i in range(10, -1, -1):
    print(i)
    
    