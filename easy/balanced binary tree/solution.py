from typing import Optional
from utils import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getBalancedHeight(root, height):
            if not root:
                return height
            left = getBalancedHeight(root.left, height + 1)
            right = getBalancedHeight(root.right, height + 1)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right)

        return getBalancedHeight(root, 0) >= 0


s = Solution()
print(s.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
