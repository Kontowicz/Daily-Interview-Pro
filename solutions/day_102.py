class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def get_level(root, node, level):
    if root == None:
        return 0
    if root.value == node:
        return level

    left_level = get_level(root.left, node, level + 1)

    if left_level != 0:
        return left_level

    return get_level(root.right, node, level + 1)

def list_cousins(tree, val):
    to_return = []
    level = get_level(tree, val, 1)

    def get_cousins(root, node, level):
        if root == None or level < 2:
            return

        if level == 2:
            if root.left:
                if root.left.value != node:
                    to_return.append(root.left.value)
            if root.right:
                if root.right.value != node:
                    to_return.append(root.right.value)
        elif level > 2:
            get_cousins(root.left, node, level - 1)
            get_cousins(root.right, node, level - 1)

    get_cousins(tree, val, level)
    return to_return

#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

assert list_cousins(root, 5).sort() == [4, 6].sort()
print(list_cousins(root, 5))
print('Test pass.')