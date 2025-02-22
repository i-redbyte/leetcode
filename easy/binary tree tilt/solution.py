from typing import Optional
from utils import TreeNode


class Solution:
    def __init__(self):
        self.total_tilt = 0

    def tree_sum(self, node: TreeNode) -> int:
        if not node:
            return 0
        left = self.tree_sum(node.left)
        right = self.tree_sum(node.right)
        tilt = abs(left - right)
        self.total_tilt += tilt
        return left + right + node.val

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tree_sum(root)
        return self.total_tilt


s = Solution()
print(s.findTilt(TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))))
