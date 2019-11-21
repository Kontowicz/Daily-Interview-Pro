class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def zigzag_order(tree):
  levels = [[tree]]
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

  to_return = []

  for i in range(0, len(levels)):
    if i % 2 == 0:
      for item in levels[i]:
        to_return.append(item.value)
    else:
      for item in levels[i][::-1]:
        to_return.append(item.value)

  return to_return
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

assert zigzag_order(n1) == [1, 3, 2, 4, 5, 6, 7]
print(zigzag_order(n1))
print('Test pass.')
# [1, 3, 2, 4, 5, 6, 7]