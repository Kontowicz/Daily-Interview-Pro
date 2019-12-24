class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"(Value: {self.value} Left: {self.left} Right: {self.right})"

def are_equal(s, t):
    if s == None and t == None:
        return True
    if s != None or t != None:
        return False

    return (s.value == t.value and are_equal(s.left, t.left) and
            are_equal(s.right, t.right))

def find_subtree(s, t):
    if s == None:
        return True
    if t == None:
        return True

    if are_equal(s, t):
        return True

    return find_subtree(s, t.left) or find_subtree(s, t.right)

t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(2))
"""
Tree t:
    1
   / \
  4   5 
 / \ / \
3  2 4 -1

Tree s:
  4 
 / \
3  2 
"""

print(find_subtree(s, t))
# True