class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def largest_path_sum(tree):
    def get_path(node, path=[], current_sum=0):
        if node.left == None and node.right == None:
            return current_sum + node.value, path + [node.value]
        left_sum = 0
        right_sum = 0
        if node.left:
            left_sum, left_path = get_path(node.left, path + [node.value], current_sum + node.value)
        if node.right:
            right_sum, right_path = get_path(node.right, path + [node.value], current_sum + node.value)

        return (left_sum, left_path) if left_sum > right_sum else (right_sum,right_path)

    return get_path(tree)[1]

tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.left.right = Node(5)
#    1
#  /   \
# 3     2
#  \   /
#   5 4
assert largest_path_sum(tree) == [1, 3, 5]
print(largest_path_sum(tree))
print('Test pass.')