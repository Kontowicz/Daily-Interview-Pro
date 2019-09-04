class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val

def height(root):
    if not root:
        return 0

    left = height(root.left)
    right = height(root.right)

    return max(left, right) + 1

def deep(root, level):
    if not root:
        return

    if level == 1:
        print(root.val)
    elif level > 1:
        deep(root.left, level - 1)
        deep(root.right, level - 1)

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

deep(root, height(root))