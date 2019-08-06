class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def ceil(root, value):
    if root == None:
        return -1

    if root.value == value:
        return root.value
    if root.value < value:
        return ceil(root.right, value)

    val = ceil(root.left, value)

    return val if val >= value else root.value


def floor(root, value):
    if root == None:
        return -1

    if root.value == value:
        return root.value
    if root.value > value:
        return floor(root.left, value)

    val = floor(root.right, value)
    return val if (val <= value) else root.value

def findCeilingFloor(root_node, k):
    return [floor(root_node, k), ceil(root_node, k)]

root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 5))