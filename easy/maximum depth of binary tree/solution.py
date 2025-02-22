from collections import deque
from typing import Optional
from utils import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        if root is None:
            return 0
        result, n2 = 1, 1
        while q:
            for _ in range(n2):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            n2 = len(q)
            if n2 != 0:
                result += 1
        return result

    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth1(root.left)
        right_depth = self.maxDepth1(root.right)
        return max(left_depth, right_depth) + 1


s = Solution()
tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.maxDepth(tree1))
tree2 = TreeNode(1, None, TreeNode(2))
print(s.maxDepth(tree2))
