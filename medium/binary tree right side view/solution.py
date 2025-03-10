from utils import TreeNode

from typing import Optional, List


class Solution:
    def rightSideView(self, root):
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)

        view = []
        collect(root, 0)
        return view

    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]


# [1, 2, 3, None, 5, None, 4]
tree1 = TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(Solution().rightSideView(tree1))
# [1, None, 3]
tree2 = TreeNode(1, None, TreeNode(3))
print(Solution().rightSideView(tree2))
print(Solution().rightSideView([]))
tree3 = TreeNode(1, TreeNode(2))
print(Solution().rightSideView(tree3))
