def findRanges(nums):
    start = None

    tmp_data = []

    for i in range(0, len(nums)):
        if start == None:
            start = i
        if i < len(nums) - 1:
            if nums[i] + 1 != nums[i + 1] and nums[i] != nums[i + 1]:
                tmp_data.append(nums[start:i+1])
                start = None
        if i == len(nums) - 1:
            if start == i:
                tmp_data.append([nums[i]])
            else:
                tmp_data.append(nums[start:i])

    to_return = []
    for item in tmp_data:
        if len(item) == 1:
            to_return.append('{}->{}'.format(item[0], item[0]))
        else:
            to_return.append('{}->{}'.format(item[0], item[len(item) - 1]))
    return to_return

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
assert findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]) == ['0->2', '5->5', '7->11', '15->15']
print('Test pass.')
