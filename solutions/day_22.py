
class Node():
	def __init__(self, val):
		self.val = val
		self.next = None
	
def print_list(root):
	while root:
		print(root.val)
		root = root.next

def intersection(a, b):
	tmp_b = b
	while a:
		while b:
			if a.val == b.val:
				return a
			b = b.next
		b = tmp_b
		a = a.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)

print_list(c)
