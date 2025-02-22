from typing import Optional
from utils import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp


s = Solution()
l = s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
while l:
    print(l.val)
    l = l.next
