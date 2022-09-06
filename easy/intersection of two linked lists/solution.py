from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        while a != b:
            a = headB if a is not None else a.next
            b = headA if b is not None else b.next
        return a

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA, currB = headA, headB
        while currA or currB:
            if currA:
                currA = currA.next
            else:
                headB = headB.next
            if currB:
                currB = currB.next
            else:
                headA = headA.next
        while headA is not headB:
            headA = headA.next
            headB = headB.next
        return headA

    def changeSign(self, head: ListNode):
        while head:
            head.val *= -1
            head = head.next

    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
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
