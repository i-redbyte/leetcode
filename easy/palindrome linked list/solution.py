from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        rabbit = head
        turtle = head
        while rabbit is not None and rabbit.next is not None:
            turtle = turtle.next
            rabbit = rabbit.next.next
        turtle = self.reverse(turtle)
        rabbit = head
        while turtle:
            if turtle.val != rabbit.val:
                return False
            turtle = turtle.next
            rabbit = rabbit.next

        return True

    def reverse(self, node):
        current = node
        previous = None
        while current:
            currentNext = current.next
            current.next = previous
            previous = current
            current = currentNext
        return previous


s = Solution()
l = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(s.isPalindrome(l))
ll = ListNode(1, ListNode(2))
print(s.isPalindrome(ll))
