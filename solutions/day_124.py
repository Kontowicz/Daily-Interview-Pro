class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def tree_level_max_sum(root):
    levels = []
    levels.append([root])

    while True:
        p = levels[-1]

        tmp = []
        for item in p:
            if item.left != None:
                tmp.append(item.left)
            if item.right != None:
                tmp.append(item.right)

        if tmp == []:
            break
        levels.append(tmp)

    sum_at_level = []
    for item in levels:
        level_sum = 0
        for elem in item:
            level_sum += elem.value
        sum_at_level.append(level_sum)

    return sum_at_level.index(max(sum_at_level))

n3 = Node(4, Node(3), Node(2))
n2 = Node(5, Node(4), Node(-1))
n1 = Node(1, n2, n3)

"""
    1          Level 0 - Sum: 1
   / \
  4   5        Level 1 - Sum: 9 
 / \ / \
3  2 4 -1      Level 2 - Sum: 8

"""
assert tree_level_max_sum(n1) == 1
print(tree_level_max_sum(n1))
print('Test pass.')