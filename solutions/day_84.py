class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)

    if left > right:
        return left + 1
    return right + 1

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

def minimum_level_sum(root):
    h = height(root)
    levels = []
    for i in range(1, h+1):
        levels.append(sum(vath(root, i)))
    return min(levels)


#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

assert minimum_level_sum(node) == 7
print(minimum_level_sum(node))
print('Test pass.')