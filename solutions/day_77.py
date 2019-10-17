class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findMax(root):
    if root is None:
        return 0

    left = findMax(root.left)
    right = findMax(root.right)

    max_value = max(max(left, right) + root.value, root.value)

    max_top_value = max(max_value, left + right + root.value)

    findMax.val = max(findMax.val, max_top_value)

    return max_value

def maxPathSum(root):
    findMax.val = float('-inf')
    findMax(root)
    return findMax.val

# (* denotes the max path)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
assert maxPathSum(root) == 42
print(maxPathSum(root))
print('Test pass.')
# 42