
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val

    left = evaluate(root.left)
    right = evaluate(root.right)

    if root.val == PLUS:
        return left + right
    elif root.val == MINUS:
        return left - right
    elif root.val == TIMES:
        return left * right
    elif root.val == DIVIDE:
        return left / right

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)

assert evaluate(tree) == 45
print(evaluate(tree))
print('Test pass.')