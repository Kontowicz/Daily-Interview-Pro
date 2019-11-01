from collections import defaultdict

class Node:
  def __init__(self, value):
    self.adjacent = []
    self.value = value

def reverse_graph(graph):
    to_return = {}

    for key, value in graph.items():
        if value == []:
            to_return[Node(key)] = []
        for item in value.adjacent:
            if item.value not in to_return:
                n = Node(item.value)
                n.adjacent = [Node(key)]
                to_return[item.value] = n
            else:
                to_return[item.value].adjacent = to_return[item.value].adjacent + [Node(key)]
    print(to_return)
    return to_return

a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

for _, val in reverse_graph(graph).items():
    for item in val.adjacent:
        if item == []:
            print('[]')
        print(item.value, end = ' ')
    print()
# []
# ['a', 'b']
# ['a']
