from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        while root:
            if root.left:
                prev, is_left = root.left, True
                while prev.right and prev.right != root:
                    prev = prev.right
                if not prev.right:
                    prev.right = root
                    root = root.left
                else:
                    prev.right = None
                    if prev == root.left and not prev.left:
                        result = result + prev.val
                    root = root.right
            else:
                root = root.right
        return result


s = Solution()
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.sumOfLeftLeaves(tree))
