class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def _repr(self, level=0):
        result = "  " * level + f"{self.value}\n"
        for child in self.children:
            result += child._repr(level + 1)
        return result

    def __repr__(self):
        return self._repr()

class GeneralTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, parent, child, current_node = None):
        if(current_node is None):
            current_node = self.root
        if(self.root is None):
            new_parent = Node(parent)
            new_child = Node(child)
            self.root = new_parent
            self.root.children.append(new_child)
        else:
            if(current_node.value == parent):
                current_node.children.append(Node(child))
                return True
            else:
                for ch in current_node.children:
                    if(self.insert(parent, child, ch) == True):
                      return True

    def traverse(self, current_node = None):
      if(current_node is None):
        current_node = self.root

      print(current_node.value)
      for ch in current_node.children:
        self.traverse(ch)
        
    def buscar(self, num, current_node = None):
      if current_node is None:
        current_node = self.root
      if self.root is None:
        return 'No hay nodos'
      else:
        if current_node.value == num:
          return True
        else:
          for ch in current_node.children:
            if self.buscar(num, ch) == True:
              return True

    def eliminar_con_hijos(self, num, current_node = None):
      if current_node is None:
        current_node = self.root
      if self.root is None:
        return 'No hay nodos'
      else:
        if current_node.value == num:
          return True
        else:
          for i in range(len(current_node.children)):
            if current_node.children[i].value == num:
              current_node.children.pop(i)
              return True
            if self.eliminar_con_hijos(num, current_node.children[i]) == True:
              return True
            
    def eliminar_sin_hijos(self, num, current_node = None):
      if current_node is None:
        current_node = self.root
      if self.root is None:
        return 'No hay nodos'
      else:
        if current_node.value == num:
          return True
        else:
          for i in range(len(current_node.children)):
            if current_node.children[i].value == num:
              current_node.children += current_node.children[i].children
              current_node.children.pop(i)
              return True
            if self.eliminar_sin_hijos(num, current_node.children[i]) == True:
              return True

    def __repr__(self):
        return self.root._repr() if self.root else "<árbol vacío>"

gt = GeneralTree()
gt.insert(4,1)
gt.insert(4,2)
gt.insert(4,3)
gt.insert(4,5)
gt.insert(1, 10)
gt.insert(2, 11)
gt.insert(10, 12)
gt.insert(5, 10)
gt.insert(10, 66)
gt.insert(10, 54)
gt.insert(2, 54)
gt.insert(12, 54)
gt.insert(54, 540)
gt.insert(540, 541)
gt.insert(10, 666)
print(gt)

print(gt.buscar(666))
print(gt.buscar(10))

print(gt.eliminar_sin_hijos(12))
print(gt)