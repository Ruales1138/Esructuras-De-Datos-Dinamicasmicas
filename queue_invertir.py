class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, n):
        self.queue.append(n)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def fist(self):
        return self.queue[0]
    
def invertir_cola(cola):
    pass
    
    
q = Queue()
print(q.queue)
q.enqueue(3)
print(q.queue)
q.enqueue(4)
print(q.queue)
q.enqueue(5)
print(q.queue)
q.dequeue()
print(q.queue)
q.dequeue()
print(q.queue)