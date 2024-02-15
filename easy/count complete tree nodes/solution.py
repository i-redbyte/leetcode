from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

    def countNodes(self, root: TreeNode) -> int:
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


