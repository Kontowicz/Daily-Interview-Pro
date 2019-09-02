def capacity(arr):
    left = [0] * len(arr)
    right = [0] * len(arr)

    water = 0

    left[0] = arr[0]

    for i in range(1, len(arr)):
        left[i] = max(left[i-1], arr[i])

    right[len(arr)-1] = arr[len(arr)-1]
    for i in range(len(arr) - 2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    for i in range(0, len(arr)):
        water += min(left[i], right[i]) - arr[i]

    return water

print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
assert capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
print('Test pass.')