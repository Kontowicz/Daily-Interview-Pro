class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def print_level_order(root):
    if root is None:
        return

    q = []

    q.append(root)

    while len(q) > 0:
        print(q[0].val)
        node = q.pop(0)


        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)