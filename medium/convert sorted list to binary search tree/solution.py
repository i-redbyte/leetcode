# Definition for singly-linked list.
from typing import Optional
from utils import TreeNode, printTree, ListNode


def get_middle(head: ListNode) -> ListNode:
    fast = head
    slow = head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    if prev:
        prev.next = None
    return slow


class Solution:

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        middle = get_middle(head)
        root = TreeNode(middle.val)
        root.right = self.sortedListToBST(middle.next)
        middle.next = None
        root.left = self.sortedListToBST(head)
        return root


s = Solution()
# [-10,-3,0,5,9]
list = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
printTree(s.sortedListToBST(list), 0)
