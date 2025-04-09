class Node:
    def __init__(self, value):
        self.value = value
        self.children: list[Node] = []
        
    def __len__(self):
        return len(self.children)
        
    def __repr__(self):
        return f'{self.value} - {self.children}'
    
    
class GeneralTree:
    def __init__(self):
        self.root : Node = None
    
    def insert(self, parent, child, flag = True):
        if self.root == None:
            self.root = Node(parent)
            self.root.children.append(Node(child))
            return
            
        else:
            if flag == True:
                current = self.root
            else:
                current = self.root.children[1]
                
            for _ in range(10):
                if current.value == parent:
                    current.children.append(Node(child))
                    return
                else:
                    current = current.children[0]
                    
            self.insert(parent, child, flag=False)
            
            
    def __repr__(self):
        return f'{self.root}'
    
a = GeneralTree()
a.insert(10, 3)
print(a)
a.insert(10, 4)
print(a)
a.insert(3, 6)
print(a)
a.insert(6, 7)
print(a)
a.insert(4, 7)
print(a)