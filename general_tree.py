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
                return True #avisé que agregué
            else:
                for ch in current_node.children:
                    if(self.insert(parent, child, ch)): #True, None
                      return True
                return False

    def traverse(self, current_node = None):
      if(current_node is None):
        current_node = self.root

      print(current_node.value)
      for ch in current_node.children:
        self.traverse(ch)

    def delete(self, value, current_node = None):
      if(current_node is None):
        current_node = self.root
      #preguntas para el current?
      for ch in current_node.children:
        #preguntas para los hijos?
        if(ch.value == value):
          current_node.children += ch.children
          current_node.children.remove(ch)
          return True
        if(self.delete(value, ch) == True): #saltando
          return True
      return False

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
print(gt)
gt.delete(10)
print(gt)