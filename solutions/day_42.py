
class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
    if root == None:
        return
    if height == 1:
        return root.value
    if root.left != None and root.right != None:
        return valuesAtHeight(root.left, height - 1), valuesAtHeight(root.right, height - 1)
    if root.left == None and root.right != None:
        return valuesAtHeight(root.right, height - 1)
    return valuesAtHeight(root.left, height - 1)

def vath(root, height):
    level = []
    counter = 1
    level.append(root)
    while height != counter:
        n = len(level)
        for item in level:
            if item.left != None:
                level.append(item.left)
            if item.right != None:
                level.append(item.right)
        counter += 1
        level = level[n::]
    result = []
    for item in level:
        result.append(item.value)
    return result


#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
#print(valuesAtHeight(a, 3))
assert vath(a, 3) == [4, 5, 7]
print(vath(a, 3))
print('Test pass.')
# [4, 5, 7]