def longest_consecutive(nums):
    to_return = []
    counter = 0
    hash = set(nums)

    for num in nums:
        if (num - 1) in hash:
            counter = 2
            tmp_val = num + 2
            while tmp_val in hash:
                counter += 1
                tmp_val += 1
            to_return.append(counter)
            counter = 0
        elif num in hash:
            counter = 1
            tmp_val = num + 1
            while tmp_val in hash:
                counter += 1
                tmp_val += 1
            to_return.append(counter)
            counter = 0

    return max(to_return)
assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
print(longest_consecutive([100, 4, 200, 1, 3, 2]))
print('Test pass.')