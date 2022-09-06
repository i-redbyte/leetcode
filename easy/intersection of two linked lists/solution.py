from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def changeSign(self, head: ListNode):
        while head:
            head.val *= -1
            head = head.next

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        self.changeSign(headA)
        while headB:
            if headB.val < 0:
                break
            headB = headB.next
        self.changeSign(headA)
        return headB


s = Solution()
listA = ListNode(2)
listA.next = ListNode(6)
listA.next.next = ListNode(4)
listB = ListNode(1)
listB.next = ListNode(5)
result = s.getIntersectionNode(listA, listB)
print(result)

