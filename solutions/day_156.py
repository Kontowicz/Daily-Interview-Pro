def majority_element(nums):
    counter = {}

    for item in nums:
        if item in counter:
            counter[item] = counter[item] + 1
        else:
            counter[item] = 1

    counter = [[k,v] for k,v in counter.items()]
    counter.sort(key = lambda x:x[1], reverse=True)

    return counter[0][0]

assert majority_element([3, 5, 3, 3, 2, 4, 3]) == 3
print(majority_element([3, 5, 3, 3, 2, 4, 3]))
print('Test pass.')