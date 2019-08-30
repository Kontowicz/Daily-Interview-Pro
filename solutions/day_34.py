def max_subarray_sum(arr):
	to_return = arr[0]
	max_sum = arr[0]
	
	for i in range(1, len(arr)):
		max_sum = max(arr[i], max_sum + arr[i])
		to_return = max(max_sum, to_return)

	return to_return

assert max_subarray_sum([34, -50, 42, 14, -5, 86]) == 137
print('Test pass')