# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        # Fill this in.
        to_return = ''
        while l1 is not None or l2 is not None:
            if l1 is None:
                first = 0
            else:
                first = l1.val

            if l2 is None:
                second = 0
            else:
                second = l2.val

            c += (int(first) + int(second))
            add = c % 10
            c = c // 10

            to_return += str(add)

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        to_return = to_return[::-1]
        root = ListNode(int(to_return[0]))

        for num in to_return[1::]:
            tmp = ListNode(int(num))
            tmp.next = root
            root = tmp

        return root



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next