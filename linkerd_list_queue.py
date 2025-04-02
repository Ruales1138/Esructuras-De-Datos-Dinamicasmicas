class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next


class LinkedList:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__size: int = 0

    def append(self, value):
        new_node = Node(value)
        if(self.__size == 0):
          self.__head = new_node 
          self.__tail = new_node 
        else:
          self.__tail.next = new_node
          self.__tail = new_node
        self.__size += 1
        
    def append_fist(self, value):
        
        new_node = Node(value)
        
        if(self.__size == 0):
            self.__head = new_node 
            self.__tail = new_node 
            
        else:
            current_node = self.__head
            new_node.next = current_node
            self.__head = new_node
            
        self.__size += 1 

    def traverse(self, current_node=None, flag = True):
        if(flag):
          current_node = self.__head
        if(current_node is None):
          return
        print(current_node.value)
        current_node = current_node.next
        self.traverse(current_node, False)
    
    def delete_first(self):
        
        if(self.__size == 0):
            return
      
        elif(self.__size == 1):
            self.__head = None
            self.__tail = None 
          
        else:
            current_node = self.__head
            self.__head = current_node.next
            current_node.next = None
            
        self.__size -= 1
        return current_node.value

    def delete_end(self):
        if(self.__size == 0):
          return
        elif(self.__size == 1):
          self.__head = None
          self.__tail = None
        else:
          current_node = self.__head
          while(current_node.next.next is not None):
            current_node = current_node.next
          current_node.next = None
          self.__tail = current_node
        self.__size -= 1
        
    def return_firs(self):
        return self.__head.value

    def __repr__(self):
        repr = ""
        current_node = self.__head
        while(current_node is not None):
          repr += str(current_node.value) + "->"
          current_node = current_node.next

        return f"{repr}"


class Queue:
    def __init__(self):
        self.queue = LinkedList()
    
    def enqueue(self, value):
        self.queue.append(value)
        
    def dequeue(self):
        self.queue.delete_first()
        
    def first(self):
        return self.queue.return_firs()
        

class Stack:
    def __init__(self):
        self.stack = LinkedList()
        
    def push(self, value):
        self.stack.append_fist(value)   
        
    def pop(self):
        return self.stack.delete_first()
        
    def top(self):
        return self.stack.return_firs()
    
        
q = Queue()
q.enqueue(5)
print(q.queue)
q.enqueue(10)
print(q.queue)
q.enqueue(9)
print(q.queue)
q.enqueue(1)
print(q.queue)
q.enqueue(93)
print(q.queue)
q.dequeue()
print(q.queue)
q.dequeue()
print(q.queue)
q.dequeue()
print(q.queue)
print(q.first())

print ('---------------------------')

s = Stack()
s.push(5)
print(s.stack)
s.push(6)
print(s.stack)
s.push(2)
print(s.stack)
s.push(1)
print(s.stack)
s.push(9)
print(s.stack)
print(s.pop())
print(s.stack)
