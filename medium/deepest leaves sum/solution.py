from typing import Optional
from utils import TreeNode


class Solution:
    def __init__(self):
        self.result = 0
        self.maxLevel = 0

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def sum(root: TreeNode, lvl: int):
            if root.left is None and root.right is None:
                if lvl > self.maxLevel:
                    self.maxLevel = lvl
                    self.result = root.val
                    return
                elif lvl == self.maxLevel:
                    self.result = self.result + root.val
                    return
                else:
                    return
            elif root.right is None and root.left is not None:
                sum(root.left, lvl + 1)
            elif root.left is None and root.right is not None:
                sum(root.right, lvl + 1)
            else:
                sum(root.left, lvl + 1)
                sum(root.right, lvl + 1)
            return

        sum(root, 0)
        return self.result


s = Solution()
t = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)),
             TreeNode(3, None, TreeNode(6, None, TreeNode(8))))
print(s.deepestLeavesSum(t))
