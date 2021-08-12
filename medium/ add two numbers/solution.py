# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        a = l1
        b = l2
        current = head
        c = 0
        while a or b:
            x = a.val if a else 0
            y = b.val if b else 0
            xy_sum = c + x + y
            c = xy_sum // 10
            current.next = ListNode(xy_sum % 10)
            current = current.next
            if a is not None:
                a = a.next
            if b is not None:
                b = b.next
        if c > 0:
            current.next = ListNode(c)
        return head.next


s = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))
result = s.addTwoNumbers(l1, l2)
while result.next:
    print(result.val)
    result = result.next
print(result.val)
