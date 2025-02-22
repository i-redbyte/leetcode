from typing import Optional
from utils import ListNode


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        rabbit = head
        turtle = head
        while k > 1:
            rabbit = rabbit.next
            k -= 1
        node_a = rabbit
        while rabbit.next:
            rabbit = rabbit.next
            turtle = turtle.next
        turtle.val, node_a.val = node_a.val, turtle.val
        return head


s = Solution()

l = s.swapNodes(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
while l:
    print(l.val)
    l = l.next
