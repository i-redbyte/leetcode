from typing import Optional
from utils import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        tortoise = head
        rabbit = head
        while rabbit is not None and rabbit.next is not None:
            rabbit = rabbit.next.next
            tortoise = tortoise.next
            if tortoise == rabbit:
                return True
        return False


s = Solution()
l = ListNode(3)
l.next = ListNode(2)
l.next.next = ListNode(0)
l.next.next.next = ListNode(-4)
l.next.next.next.next = l.next
print(s.hasCycle(l))
