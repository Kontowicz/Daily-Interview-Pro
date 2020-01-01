class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __repr__(self):
    return f"({self.value}, {self.next})"


def remove_dup(lst):
    to_return = lst
    if lst is None or lst.next is None:
        return lst

    while lst.next is not None:
        if lst.value == lst.next.value:
            new = lst.next.next
            lst.next = None
            lst.next = new
        else:
            lst = lst.next

    return to_return

lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

remove_dup(lst)
print(lst)
# (1, (2, (3, None)))