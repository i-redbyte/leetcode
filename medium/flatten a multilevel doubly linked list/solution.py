# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Optional[Node]:
        if not head:
            return
        tmp = Node(0, None, head, None)
        stack = [head]
        prev = tmp
        while stack:
            root = stack.pop()
            root.prev = prev
            prev.next = root
            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root
        tmp.next.prev = None
        return tmp.next


s = Solution()
print(s.flatten(Node(None, None, None, None)))
