class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def min_depth_bst(root):
    def break_condiotion(arr):
        for item in arr:
            if item.left == None and item.right == None:
                return False
        return True

    cnt = 0

    first = [root]
    next = []

    while break_condiotion(first):
        for item in first:
            if item.left != None:
                next.append(item.left)
            if item.right != None:
                next.append(item.right)
        first = next
        next = []
        cnt += 1

    return cnt


n3 = Node(3, None, Node(4))
n2 = Node(2, Node(3))
n1 = Node(1, n2, n3)

#     1
#    / \
#   2   3
#        \
#         4

assert min_depth_bst(n1) == 2
print(min_depth_bst(n1))
print('Test pass.')