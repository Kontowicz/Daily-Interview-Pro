def reverseWords(str):
	return ' '.join(word[::-1] for word in str.split(' '))


assert reverseWords("The cat in the hat") == 'ehT tac ni eht tah'
print('Test pass.')
# ehT tac ni eht tah