def search(matrix, word, x, y):
	if word == '':
		return True
	
	if matrix[x][y + 1] == word[0]:
		return search(matrix, word[1::], x, y + 1)
	
	if matrix[x + 1][y] == word[0]:
		return search(matrix, word[1::], x + 1, y)
		
	return False

def word_search(matrix, word):
	results = []
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[i])):
			if matrix[i][j] == word[0]:
				if search(matrix, word[1::], i, j) == True:
					return True
	
	return False
  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
  
assert word_search(matrix, 'FOAM') == True

matrix = [
  ['F', 'O', 'A', 'M'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
  
assert word_search(matrix, 'FOAM') == True

matrix = [
  ['F', 'o', 'A', 'M'],
  ['D', 'O', 'Q', 'P'],
  ['A', 'N', 'A', 'B'],
  ['M', 'A', 'S', 'M']]
  
assert word_search(matrix, 'FOAM') == False

print('Test pass.')