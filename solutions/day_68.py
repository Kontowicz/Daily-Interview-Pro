def hIndex(publications):
    publications.sort(reverse=True)

    start = 0
    cnt = 0
    while start < len(publications) and start < publications[start]:
        cnt += 1
        start += 1

    return cnt

assert hIndex([5, 3, 3, 1, 0]) == 3
print(hIndex([5, 3, 3, 1, 0]))
print('Test pass.')