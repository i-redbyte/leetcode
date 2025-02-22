from typing import Optional
from utils import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = current_head = ListNode(0)
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current_head.next = list1
                current_head = current_head.next
                list1 = list1.next
            else:
                current_head.next = list2
                current_head = current_head.next
                list2 = list2.next
        if list1 is not None:
            current_head.next = list1
        if list2 is not None:
            current_head.next = list2
        return head.next


s = Solution()
l1 = ListNode(1, ListNode(2, ListNode(4, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, ListNode(5))))
res = s.mergeTwoLists(l1, l2)

print("Result:")
while res is not None:
    print(res.val)
    res = res.next

