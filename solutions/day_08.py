def two_sum(list, k):
	list.sort()
	
	begin = 0
	end = len(list) - 1

	while begin < end:
		sum = list[begin] + list[end]
		if sum == k:
			return True
		elif sum > k:
			end -= 1
		else:
			begin += 1
			
	return False
	
	
print(two_sum([4,7,1,-3,2], 5))
assert two_sum([4,7,1,-3,2], 5) == True
print('Test pass')