# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        while tmp:
            if tmp.next is not None and tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head


s = Solution()
l1 = ListNode(1, ListNode(1, ListNode(2, None)))
s.deleteDuplicates(l1)
