from collections import deque

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value
  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      num = len(q)
      while num > 0:
        n = q.popleft()
        result += str(n.value)
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
        num = num - 1
      if len(q):
        result += "\n"

    return result
def fullBinaryTree(node):
    if node == None:
        return None
    node.left = fullBinaryTree(node.left)
    node.right = fullBinaryTree(node.right)

    if node.left == None and node.right == None:
        return node

    if node.left == None:
        new = node.right
        tmp = node
        node = None
        del(tmp)
        return new

    if node.right == None:
        new = node.left
        tmp = node
        node = None
        del(tmp)
        return new
    return node

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)
print(fullBinaryTree(tree))
# 1
# 03
# 94