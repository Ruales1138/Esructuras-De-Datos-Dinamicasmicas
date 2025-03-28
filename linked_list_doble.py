class DoubleNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
    
    def __repr__(self):
       return str(self.value)


class DoubleLinkedList:
    def __init__(self):
        self.__head: DoubleNode = None
        self.__tail: DoubleNode = None
        self.__size: int = 0


    def append(self, value):
        new_node = DoubleNode(value)
      
        if(self.__size == 0):
            self.__head = new_node 
            self.__tail = new_node 
          
        else:
            node_anterior = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node
            self.__tail.prev = node_anterior
          
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
        
    def append_whit_position(self, value, position, current_node = None, flag = True, counter = 0):
        if position <= self.__size:
            counter += 1
            
            if(flag):
                current_node = self.__head
                
            if(counter == position):
                #new_node = DoubleNode(value)
                if self.__size == position:
                    self.append(value)
                    return
                
                
                
                return
        
            self.append_whit_position(value, position, current_node.next, False, counter)
        
        else:
            return 'No existe'
      
    def delete_whit_position(self, posotion):
        pass

    def __repr__(self):
        repr = ""
        current_node = self.__head

        while(current_node is not None):
            repr += "(" + str(current_node.prev) + "<-" + str(current_node) + "->" + str(current_node.next) + ')'
            current_node = current_node.next

        return f"{repr}"


ll = DoubleLinkedList()
ll.append(5)
ll.append(1)
ll.append(4)
ll.append(7)
print(ll)
#ll.delete_end()
#print("---")
#print(ll)
#ll.delete_end()
#print("---")
#print(ll)
#ll.delete_end()
#print("---")
#print(ll)
#ll.delete_end()
print("---")

ll.append_whit_position(5, 4)
print(ll)
ll.append_whit_position(2, 1)
print(ll)