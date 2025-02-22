from utils import TreeNode
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

    def isSameTree1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


s = Solution()

tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.isSameTree(tree1, tree2))
tree1 = TreeNode(1, TreeNode(2))
tree2 = TreeNode(1, None, TreeNode(2))
print(s.isSameTree(tree1, tree2))
tree1 = TreeNode(1, TreeNode(2), TreeNode(1))
tree2 = TreeNode(1, TreeNode(1), TreeNode(2))
print(s.isSameTree(tree1, tree2))
