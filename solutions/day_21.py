def num_ways(n, m):
	if n == 1 or m == 1:
		return 1
		
	return num_ways(n - 1, m) + num_ways(n, m - 1)

def num_ways_opt(n, m):
	
	way = [[1 for i in range(m)] for j in range(n)]
	
	for i in range(1, n):
		for j in range(1, m):
			way[i][j] = way[i-1][j] + way[i][j-1]
			
	return way[n-1][m-1]
	
assert num_ways_opt(2,2) == 2
