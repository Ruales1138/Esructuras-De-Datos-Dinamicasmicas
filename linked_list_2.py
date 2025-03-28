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

  def traverse(self, current_node=None, flag = True):
    if(flag):
      current_node = self.__head
    if(current_node is None):
      return
    print(current_node.value)
    current_node = current_node.next
    self.traverse(current_node, False)

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

  def __repr__(self):
    repr = ""
    current_node = self.__head
    while(current_node is not None):
      repr += str(current_node.value) + "->"
      current_node = current_node.next

    return f"{repr}"

ll = LinkedList()
ll.append(5)
ll.append(1)
ll.append(4)
ll.append(7)
print(ll)
ll.delete_end()
print("---")
print(ll)
ll.delete_end()
print("---")
print(ll)
ll.delete_end()
print("---")
print(ll)
ll.delete_end()
print("---")