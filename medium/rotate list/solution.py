# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        size = 1
        while cur.next:
            size += 1
            cur = cur.next
        k %= size
        if k == 0:
            return head
        cur.next = head

        cur = head
        for _ in range(size - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None

        return new_head


s = Solution()
head = ListNode(0, ListNode(1, ListNode(2, None)))
res = s.rotateRight(head, 4)
print("List one:")
while res.next:
    print(res.val)
    res = res.next
print(res.val)
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
res = s.rotateRight(head, 2)
print("List two:")
while res.next:
    print(res.val)
    res = res.next
print(res.val)
