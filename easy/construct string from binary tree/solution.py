from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = str(root.val)
        if root.left:
            result += "(" + self.tree2str(root.left) + ")"
        if root.right:
            if not root.left:
                result += "()"
            result += "(" + self.tree2str(root.right) + ")"
        return result

    def tree2str1(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        if root.left is None and root.right is None:
            return str(root.val)
        if root.right is None:
            return "{val}({left})".format(val=root.val, left=self.tree2str(root.left))
        return "{val}({left})({right})".format(val=root.val, left=self.tree2str(root.left),
                                               right=self.tree2str(root.right))


s = Solution()
t = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(s.tree2str(t))
