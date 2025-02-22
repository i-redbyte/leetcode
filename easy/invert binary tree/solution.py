from typing import Optional
from utils import TreeNode, printTree


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root

    def invertTree2(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root


s = Solution()
t = TreeNode(2, TreeNode(1), TreeNode(3))
printTree(t)
print()
printTree(s.invertTree(t))
