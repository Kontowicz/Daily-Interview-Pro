class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root, left = None, right = None):
    if root == None:
        return True

    if left != None and root.key <= left.key:
        return False

    if right != None and root.key >= right.key:
        return False

    return is_bst(root.left, left, root) and is_bst(root.right, root, right)

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)

assert is_bst(a) == True
print('Test pass.')
