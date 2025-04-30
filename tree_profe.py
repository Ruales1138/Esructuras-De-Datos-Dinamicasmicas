import random
class BinaryNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value, current_node = None):
    if(self.root is None):
      self.root = BinaryNode(value)
    else:
      if(current_node is None):
        current_node = self.root

      if(current_node.value == value):
        return #no se pueden repetidos
      elif(value < current_node.value):
        #pregunto si hay hijo
        if(current_node.left is None):
          #si no, me inserto
          current_node.left = BinaryNode(value)
        else:
          #si sí, salto
          self.insert(value, current_node.left)
      else:
        #pregunto si hay hijo
        if(current_node.right is None):
          #si no, me inserto
          current_node.right = BinaryNode(value)
        else:
          #si sí, salto
          self.insert(value, current_node.right)


  def print(self, node, prefix="", is_left=True):
    if not node:
      print("Empty Tree")
      return
    if node.right:
      self.print(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
    if node.left:
      self.print(node.left, prefix + ("    " if is_left else "│   "), True)

  def inorder_traversal(self, current_node = None, flag = True):
    if(flag):
      current_node = self.root

    if(current_node is None):
      return
    #left
    self.inorder_traversal(current_node.left, flag = False)
    #root
    print(current_node.value)
    #right
    self.inorder_traversal(current_node.right, flag = False)


  def preorder_traversal(self, current_node = None, flag = True):
    if(flag):
      current_node = self.root

    if(current_node is None):
      return
    #root
    print(current_node.value)
    #left
    self.preorder_traversal(current_node.left, flag = False)
    #right
    self.preorder_traversal(current_node.right, flag = False)

  def postorder_traversal(self, current_node = None, flag = True):
    if(flag):
      current_node = self.root

    if(current_node is None):
      return
    #left
    self.postorder_traversal(current_node.left, flag = False)
    #right
    self.postorder_traversal(current_node.right, flag = False)
    #root
    print(current_node.value)







random.seed(1)
bst = BinarySearchTree()
for i in range(6):
  bst.insert(random.randint(1,1000))

bst.print(bst.root)