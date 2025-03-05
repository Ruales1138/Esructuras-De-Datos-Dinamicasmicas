class Queue:
    def __init__(self, priority):
        self.queue = []
        self.priority = priority
        
    def enqueue(self, n):
        if self.priority == 'min':
            if len(self.queue) == 0:
                self.queue.append(n)
            else:
                for i in range(len(self.queue)):
                    if n < self.queue[i]:
                        self.queue.insert(i, n)
                        return
                self.queue.append(n)
        
        if self.priority == 'max':
            if len(self.queue) == 0:
                self.queue.append(n)
            else:
                for i in range(len(self.queue)):
                    if n > self.queue[i]:
                        self.queue.insert(i, n)
                        return
                self.queue.append(n)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def fist(self):
        return self.queue[0]
        
        
q = Queue('min')
#q = Queue('max')
print(q.queue)
q.enqueue(5)
print(q.queue)
q.enqueue(8)
print(q.queue)
q.enqueue(55)
print(q.queue)
q.enqueue(2)
print(q.queue)
q.enqueue(1)
print(q.queue)
q.enqueue(9)
print(q.queue)
q.enqueue(10)
print(q.queue)
q.enqueue(3)
print(q.queue)

print(q.dequeue())
print(q.queue)
print(q.dequeue())
print(q.queue)

print(q.fist())