from typing import Optional
from utils import ListNode


class Solution:
    def reverse_list(self, start: ListNode, stop: ListNode):
        prev = None
        current = start
        while current != stop:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        el = None

        while fast:
            steps = k - 1
            while fast and steps > 0:
                fast = fast.next
                steps = steps - 1

            if fast:
                tmp = fast.next
                self.reverse_list(slow, fast.next)
                if el is None:
                    head = fast
                else:
                    el.next = fast
                slow.next = tmp
                el = slow
                slow = tmp
                fast = tmp
        return head


s = Solution()

l = s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
while l:
    print(l.val)
    l = l.next
