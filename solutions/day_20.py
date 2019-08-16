
def minSubArrayLen(nums, target):
	start = 0
	end = 0
	min_len = len(nums) + 1
	curent_sum = 0
	
	while end < len(nums):
		while (curent_sum <= target and end < len(nums)):
			curent_sum += nums[end]
			end += 1
			
		while (curent_sum > target and start < len(nums)): 
			curent_sum -= nums[start] 
			start+= 1
			if (end - start < min_len): 
				min_len = end - start
			
	
	return min_len  
	
assert minSubArrayLen([2, 3, 1, 2, 4, 3], 7) == 2
print('Test pass.')