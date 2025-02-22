from typing import Optional
from utils import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        h = head
        h_next = head.next
        stack = []
        while head:
            stack.append(head)
            head = head.next
        s = stack.pop()
        s_prev = None
        while h != s_prev and s != h_next:
            s_prev = stack.pop()
            h.next = s
            s.next = h_next
            s_prev.next = None
            h = h_next
            s = s_prev
            h_next = h.next


s = Solution()
s.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
s.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
