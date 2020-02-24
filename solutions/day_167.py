def generateAllSubsets(nums):
    to_return = []
    for i in range(0, 2**len(nums)):
        bin_num = bin(i)[2:].zfill(len(nums))
        if bin_num != None:
            tmp = []
            for z, y in zip(bin_num, nums):
                if z != '0':
                    tmp.append(y)
            to_return.append(tmp)

    return to_return

assert generateAllSubsets([1, 2, 3]) == [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
print(generateAllSubsets([1, 2, 3]))
print('Test pass.')