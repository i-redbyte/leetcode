# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        left = False
        right = False
        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0
        if root.right:
            right = self.hasPathSum(root.right, targetSum)
        if root.left:
            left = self.hasPathSum(root.left, targetSum)
        return left or right


s = Solution()

tree1 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), ),
                 TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(1))))
print(s.hasPathSum(tree1, 22))

tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.hasPathSum(tree2, 5))

tree3 = TreeNode(1, TreeNode(2))
print(s.hasPathSum(tree3, 0))
