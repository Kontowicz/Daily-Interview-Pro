class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"({self.value}, {self.left}, {self.right})"


def bst_numbers_sum(root, num=''): 
    if root.left == None and root.right == None:
        return int(num+str(root.value))
    else:
        return bst_numbers_sum(root.left, num+str(root.value)) + bst_numbers_sum(root.right, num+str(root.value))

n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  / \
# 4   5

assert bst_numbers_sum(n1) == 262

print(bst_numbers_sum(n1))

print('Test pass.')
