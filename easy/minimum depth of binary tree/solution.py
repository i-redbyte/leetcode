from typing import Optional
from utils import TreeNode


class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


s = Solution()
tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.minDepth(tree1))
tree2 = TreeNode(1, None, TreeNode(2))
print(s.minDepth(tree2))
