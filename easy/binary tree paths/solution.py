from typing import Optional, List
from utils import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def computed(root: Optional[TreeNode], buffer) -> List[str]:
            if not root.left and not root.right:
                return [buffer + f"{root.val}"]

            left = right = list()

            if root.left:
                l_path = buffer + f"{root.val}" + "->"
                left = computed(root.left, l_path)

            if root.right:
                r_path = buffer + f"{root.val}" + "->"
                right = computed(root.right, r_path)
            return left + right

        return computed(root, "")


s = Solution()
t = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(s.binaryTreePaths(t))
