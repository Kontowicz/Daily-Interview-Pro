from collections import deque
class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.value
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result

pointer = 0


def reconstruct(preOrderRighteOrder, inOrder, index=None):
    if inOrder:
        if index is None:
            index = {}
            for i in range(len(inOrder)):
                index[inOrder[i]] = i

        node = Node(preOrderRighteOrder[0])
        index_num = index.get(node.value)
        inOrderLeft = inOrder[:index_num]
        inOrderRight = inOrder[index_num + 1:]
        preOrderRighteOrderLeft = [n for n in preOrderRighteOrder if index.get(n) < index_num]
        preOrderRight = [n for n in preOrderRighteOrder if index.get(n) > index_num]

        node.left = reconstruct(preOrderRighteOrderLeft, inOrderLeft)
        node.right = reconstruct(preOrderRight, inOrderRight)
        return node


tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
d = str(tree)
print(d)
assert d == 'abcdefg'
print('Test pass.')