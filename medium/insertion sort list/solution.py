# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(0)
        tmp.next = head
        while head and head.next:
            if head.val > head.next.val:
                insert_node = head.next
                prev = tmp
                while prev.next.val < insert_node.val:
                    prev = prev.next
                head.next = insert_node.next
                insert_node.next = prev.next
                prev.next = insert_node
            else:
                head = head.next
        return tmp.next


s = Solution()
linked_list = s.insertionSortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
while linked_list:
    print(linked_list.val)
    linked_list = linked_list.next
