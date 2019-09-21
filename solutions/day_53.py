def get_rooms(array):
	start_time = {}
	end_time = {}
	
	for start, end in array:
		if start not in start_time:
			start_time[start] = 0
		start_time[start] += 1
		
		if end not in end_time:
			end_time[end] = 0
		end_time[end] += 1
		
	start = min(start_time)
	end = max(end_time)
	
	cnt = 0
	total = 0
	for i in range(start, end):
		if i in start_time:
			cnt += start_time[i]
			if cnt > total:
				total = cnt
		if i in end_time:
			cnt -= end_time[i]
	
	return total
	
assert get_rooms( [(30, 75), (0, 50), (60, 150)] ) == 2
print('Test pass')