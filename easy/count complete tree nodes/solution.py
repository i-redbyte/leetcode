from typing import Optional
from utils import TreeNode


class Solution:

    def exist(self, root: TreeNode, mask: int, h: int) -> bool:
        temp = root

        for i in range(h - 1, 0, -1):
            if mask & (1 << i):
                temp = temp.right
            else:
                temp = temp.left

        if mask & 1:
            return temp.right is not None
        return temp.left is not None

    def countNodes1(self, root: TreeNode) -> int:
        if not root:
            return 0
        h = 0
        result = 0
        temp = root

        while temp.left:
            result += (1 << h)
            h += 1
            temp = temp.left

        l, r = 0, (1 << h) - 1
        lastLvl = 0
        while l <= r:
            mid = (l + r) >> 1

            if self.exist(root, mid, h):
                lastLvl = max(lastLvl, mid)
                l = mid + 1
            else:
                r = mid - 1

        result += lastLvl + 1
        return result

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count = 1
        if root.left is not None:
            count += self.countNodes(root.left)
        if root.right is not None:
            count += self.countNodes(root.right)
        return count
