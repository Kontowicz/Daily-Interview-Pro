def buy_and_sell(arr):
    to_return = 0

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] > to_return:
                to_return = arr[j] - arr[i]

    return to_return

assert buy_and_sell([9, 11, 8, 5, 7, 10]) == 5