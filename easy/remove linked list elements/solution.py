from utils import ListNode
from typing import Optional


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, current = None, head
        while current:
            if current.val == val:
                if current is head:
                    head = head.next
                else:
                    prev.next = current.next
            else:
                prev = current
            current = current.next
        return head


s = Solution()
test_list1 = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
s.removeElements(test_list1, 6)
while test_list1:
    print(test_list1.val)
    test_list1 = test_list1.next
