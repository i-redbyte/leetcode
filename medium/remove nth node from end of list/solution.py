from typing import Optional
from utils import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = r = head
        for i in range(n):
            l = l.next
        if not l:
            return head.next
        while l.next:
            l = l.next
            r = r.next
        r.next = r.next.next
        return head


s = Solution()
list = s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
while list:
    print(list.val)
    list = list.next
