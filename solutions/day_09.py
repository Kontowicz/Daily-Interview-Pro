
def singleNumber(nums):
	one_num = nums[0]
	
	for number in nums[1::]:
		one_num ^= number	
		
	return one_num

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
assert singleNumber([4, 3, 2, 4, 1, 3, 2]) == 1
print('Test pass.')