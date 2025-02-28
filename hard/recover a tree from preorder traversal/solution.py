from typing import Optional

from utils import TreeNode, printTree


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def getNextNumberAndDepth(s: str, index: int) -> (int, int, int):
            depth = 0
            n = len(s)
            while index < n and s[index] == '-':
                depth += 1
                index += 1
            num = 0
            while index < n and s[index].isdigit():
                num = num * 10 + int(s[index])
                index += 1
            return num, depth, index

        i = 0
        stack = []

        while i < len(traversal):
            val, depth, i = getNextNumberAndDepth(traversal, i)
            node = TreeNode(val)
            while len(stack) > depth:
                stack.pop()

            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)
        return stack[0]


s = Solution()
printTree(s.recoverFromPreorder("1-2--3--4-5--6--7"))
printTree(s.recoverFromPreorder("1-2--3---4-5--6---7"))
printTree(s.recoverFromPreorder("1-401--349---90--88"))
