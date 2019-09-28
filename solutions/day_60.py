class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    # pre-order printing of the tree.
    result = ''
    result += str(self.val)
    if self.left:
      result += str(self.left)
    if self.right:
      result += str(self.right)
    return result

def serialize(root):
    to_return = []

    def serialize_recursive(root):
        if root:
            to_return.append(str(root.val))
            serialize_recursive(root.left)
            serialize_recursive(root.right)
        else:
            to_return.append('#')

    serialize_recursive(root)

    return ' '.join(to_return)

def deserialize(data):
    def deserialize_recursive(vals):
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = deserialize_recursive(vals)
        node.right = deserialize_recursive(vals)
        return node

    vals = iter(data.split())
    return deserialize_recursive(vals)

#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(serialize(tree))
# 1 3 2 # # 5 # # 4 # 7 # #
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
# 132547