def witnesses(heights):
    heights.append(0)

    cnt = 0

    for i in range(0, len(heights) - 1):
        if heights[i] > heights[i + 1]:
            cnt += 1

    return cnt

print(witnesses([3, 6, 3, 4, 1]))
assert witnesses([3, 6, 3, 4, 1]) == 3
print('Test pass.')
