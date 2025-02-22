from typing import Optional
from utils import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def flattenTree(node: TreeNode) -> Optional[TreeNode]:
            if not node:
                return None

            if not node.left and not node.right:
                return node

            leftTail = flattenTree(node.left)
            rightTail = flattenTree(node.right)
            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            return rightTail if rightTail else leftTail

        flattenTree(root)
