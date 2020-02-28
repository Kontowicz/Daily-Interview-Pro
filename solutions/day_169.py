class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def is_palindrome(node):
    start = node
    end = node
    while end.next != None:
        end = end.next
    
    while end != start:
        if end.val != start.val:
            return False
        end = end.prev
        start = start.next

    return True

node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

assert is_palindrome(node) == True
print('Test pass.')

print(is_palindrome(node))