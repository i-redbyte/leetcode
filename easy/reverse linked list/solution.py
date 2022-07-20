from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        second = head.next
        third = second.next
        head.next = None
        second.next = head
        current = third
        previos = second
        while current is not None:
            next = current.next
            current.next = previos
            previos = current
            current = next
        return previos


s = Solution()
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
r = s.reverseList(l)
while r is not None:
    print(r.val)
    r = r.next
