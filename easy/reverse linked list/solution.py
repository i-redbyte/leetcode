from typing import Optional
from utils import ListNode


class Solution:
    def recursive(self, node, p):
        if not node:
            return p
        n = node.next
        node.next = p
        return self.recursive(n, node)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursive(head, None)

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or not head:
            return head
        if head.next is None:
            return head
        tmp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tmp

    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
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
r1 = s.reverseList([])
print(r1)
one1 = s.reverseList(ListNode(1, ListNode(2)))
while one1 is not None:
    print(one1.val)
    one1 = one1.next
