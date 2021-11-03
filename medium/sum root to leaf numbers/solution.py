from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def dfs(self, root: Optional[TreeNode], s: str):
        if not root:
            return
        s += str(root.val)
        self.dfs(root.left, s)
        self.dfs(root.right, s)
        if not root.left and not root.right:
            self.result += int(s)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        tmp_result = ""
        self.dfs(root, tmp_result)
        return self.result


s = Solution()
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.sumNumbers(tree1))
