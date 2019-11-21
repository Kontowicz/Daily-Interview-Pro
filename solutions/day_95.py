
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        levels = []
        levels.append([self])

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
        to_return = ''

        for item in levels:
            for e in item:
                to_return += f'{e.val} '
            to_return += '\n'

        return to_return


tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

print(tree)
# a
# bc
# defg