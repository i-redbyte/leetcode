from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(r):
            if r:
                return inorder(r.left) + [r.val] + inorder(r.right)
            else:
                return []
        return inorder(root)[k - 1]


s = Solution()
tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(s.kthSmallest(tree, 1))
