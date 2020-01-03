def num_connected_components(edges):
    to_return = []

    for edge in edges:
        push = True
        for i in range(0, len(to_return)):
            if edge[0] in to_return[i] or edge[1] in to_return[i]:
                to_return[i].add(edge[0])
                to_return[i].add(edge[1])
                push = False
                break
        if push:
            to_return.append({edge[0], edge[1]})

    return len(to_return)

assert num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6)]) == 2
print(num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6)]))
print('Test pass.')