class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def help_is_uniqie(root, value):
    if root == None:
        return True
    if root.val == value:
        return  help_is_uniqie(root.left, value) and help_is_uniqie(root.right, value)
    return False

def is_unique(root):
    return help_is_uniqie(root, root.val)

def count_unival_subtrees(root):
    if root == None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)

    if is_unique(root):
        return 1 + left + right
    return left + right

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

assert count_unival_subtrees(a) == 5
print('Test pass.')