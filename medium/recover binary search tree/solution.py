from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = TreeNode(-999999999999999)

    def recoverTree(self, root: Optional[TreeNode]) -> None:

        def inorder(node):
            if node:
                inorder(node.left)
                if self.prev.val >= node.val:
                    self.first = self.first or self.prev
                    self.second = node
                self.prev = node
                inorder(node.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val


s = Solution()
tree = TreeNode(1, TreeNode(3, None, TreeNode(2)), None)
s.recoverTree(tree)
