class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
	
	none_counter = 0

	
	sorted = []
	
	while none_counter != len(lists):
		none_counter = 0
		elem = []
		positions = []
		for i in range(0, len(lists)):
			if lists[i] == None:
				none_counter += 1
				continue

			elem.append(lists[i].val)
			positions.append(i)
		
		if elem == []:
			break
		
		pos = elem.index(min(elem))

		sorted.append(elem[pos])
		
		lists[positions[pos]] = lists[positions[pos]].next
		
	return sorted
		

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
assert merge([a, b]) == [1, 2, 3, 4, 5, 6]
print('Test pass.')
