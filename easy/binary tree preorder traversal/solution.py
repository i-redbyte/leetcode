from typing import Optional, List
from utils import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp:
                result.append(tmp.val)
                stack.append(tmp.right)
                stack.append(tmp.left)
        return result

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def preorder(node):
            if node:
                result.append(node.val)
                preorder(node.left)
                preorder(node.right)

        if not root:
            return result
        preorder(root)
        return result

    def preorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


s = Solution()
t1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(s.preorderTraversal(t1))
