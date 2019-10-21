class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def is_palindrome(node):
    left = node
    right = node

    while right.next != None:
        right = right.next

    while left != right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.prev

    return True

node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

assert is_palindrome(node) == True
print(is_palindrome(node))
print('Test pass.')