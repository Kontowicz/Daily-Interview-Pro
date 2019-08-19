class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node):
    start = node
    pointer = node

    counter = 0
    while node:
        tmp = node
        while tmp:
            counter += tmp.value
            if counter == 0:
                pointer.next = tmp.next
                pointer = tmp.next
            tmp = tmp.next
        node = node.next

    return start

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)

while node:
  print(node.value)
  node = node.next