class Queue:
    def __init__(self) -> None:
        self.cantidad: int = 0
        self.size: int = 5
        self.queue = [None] * self.size
        self.front: int = 0
        self.rear: int = 0

    def enqueue(self, elemento):
        if self.cantidad == self.size:
            return
        
        self.queue[self.rear] = elemento
        self.cantidad += 1

        if self.rear == self.size:
            self.rear = 0

        else:
            self.rear += 1

    def dequeue(self):

        elemento2 = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.size:
            self.front = 0
        else:
            self.front += 1
        return elemento2

    def __repr__(self) -> str:
        return str(self.queue)
    


queue = Queue()
print(queue)
queue.enqueue(12)
print(queue)
queue.enqueue(23)
print(queue)
queue.enqueue(15)
print(queue)
queue.enqueue(56)
print(queue)
queue.enqueue(2)
print(queue)
queue.enqueue(100)
print(queue)
queue.enqueue(10)
print(queue)

queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)

queue.enqueue(2)
print(queue)
queue.enqueue(100)
print(queue)
queue.enqueue(10)
#queue.enqueue(10)
#print(queue)