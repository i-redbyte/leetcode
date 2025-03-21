from typing import Optional
from utils import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [(root, 0)]
        while stack:
            root, current_val = stack.pop()
            if root is not None:
                current_val = (current_val << 1) | root.val
                if root.left is None and root.right is None:
                    # print(current_val)
                    result += current_val
                else:
                    stack.append((root.right, current_val))
                    stack.append((root.left, current_val))
        return result


s = Solution()
tree1 = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1)))
print(s.sumRootToLeaf(tree1))
