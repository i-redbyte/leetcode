from typing import Optional
from utils import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        tmp = ListNode(0)
        tmp.next = head
        prev = tmp

        n = left - 1
        for i in range(n):
            prev = prev.next

        reverse = None
        current = prev.next
        m = right - left + 1
        for i in range(m):
            nxt = current.next
            current.next = reverse
            reverse = current
            current = nxt

        prev.next.next = current
        prev.next = reverse
        return tmp.next


s = Solution()
list = s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)

while list:
    print(list.val)
    list = list.next
