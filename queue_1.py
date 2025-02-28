class Queue:
    def __init__(self) -> None:
        self.queue: dict = {}
        self.idx = 0
        self.idx2 = 0

    def enqueue(self, n):
        self.queue.update({str(self.idx): n})
        self.idx += 1

    def dequeue(self):
        first_num = self.queue[str(self.idx2)]
        del self.queue[str(self.idx2)]
        self.idx2 += 1
        return first_num

    def first(self):
        return self.queue[str(self.idx2)]
    
    def __repr__(self) -> str:
        return str(self.queue)
    
q = Queue()
print(q)
q.enqueue(1)
print(q)
q.enqueue(2)
print(q)
q.enqueue(4)
print(q)
q.enqueue(5)
print(q)
print(q.dequeue())
print(q)
print(q.dequeue())
print(q)

print(q.first())