from typing import Optional

from utils import TreeNode


class Solution:
    def dfs(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return 0, 0
        amount_left, max_amount_left = self.dfs(root.left)
        amount_right, max_amount_right = self.dfs(root.right)
        amount = max_amount_left + max_amount_right + root.val
        max_amount = max(amount_left, max_amount_left) + max(amount_right, max_amount_right)
        return amount, max_amount

    def rob(self, root: Optional[TreeNode]) -> int:
        pick, nopick = self.dfs(root)
        return max(pick, nopick)


s = Solution()
print(s.rob(TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))))
