class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.value) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"


def create_tree(postorder):
    head = Node(postorder[-1])

    if len(postorder) == 1:
        return head

    for i in range(0, len(postorder) - 1):
        if postorder[i] > head.value:
            s = i
            break

    less, gt = postorder[:s], postorder[s:-1]

    head.left = create_tree(less) if less else None
    head.right = create_tree(gt) if less else None

    return head

# 2 is the root node, with 1 as the left child and 3 as the right child
print(create_tree([1, 3, 2]))
