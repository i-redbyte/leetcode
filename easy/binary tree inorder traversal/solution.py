from typing import List, Optional

from utils import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        while current is not None or stack != []:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result


s = Solution()
tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(s.inorderTraversal(tree))
print(s.inorderTraversal(None))
tree = TreeNode(1, TreeNode(2))
print(s.inorderTraversal(tree))
