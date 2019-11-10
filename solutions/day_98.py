class Node():
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

def most_freq_subtree_sum(root):
    values = {}

    def subtree_sum(root):
        if root == None:
            return 0

        return (root.val + subtree_sum(root.left) + subtree_sum(root.right))

    def traverse(root):
        if root == None:
            return

        val = subtree_sum(root)
        if val in values:
            values[val] = values[val] + 1
        else:
            values[val] = 1
        traverse(root.left)
        traverse(root.right)

    traverse(root)

    return max(values.items(), key=lambda x:x[1])[0]


root = Node(3, Node(1), Node(-3))
assert most_freq_subtree_sum(root) == 1
print(most_freq_subtree_sum(root))
print('Test pass.')