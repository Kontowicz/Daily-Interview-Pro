import operator
class Node():
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def is_symetric_helper(node_first, node_second):
    if node_first.children == [] and node_second.children == []:
        return True

    first_node_children = node_first.children
    second_node_children = node_second.children

    if len(second_node_children) != len(first_node_children):
        return False

    first_node_children.sort(key=operator.attrgetter('value'))
    second_node_children.sort(key=operator.attrgetter('value'))

    for i in range(0, len(first_node_children)):
        if first_node_children[i].value != second_node_children[i].value:
            return False
        is_symetric_helper(first_node_children[i], second_node_children[i])

    return True

def is_symmetric(root):
    if len(root.children) != 2:
        return False
    return is_symetric_helper(root.children[0], root.children[1])

tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
assert is_symmetric(tree) == True
print(is_symmetric(tree))
print('Test pass.')