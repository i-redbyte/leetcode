from typing import Optional
from utils import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            l.append(node.val)
            dfs(node.right)

        dfs(root)

        n = len(l)
        for i in range(1, n):
            if l[i - 1] >= l[i]:
                return False
        return True


t = TreeNode(2, TreeNode(1), TreeNode(3))
print(Solution().isValidBST(t))
