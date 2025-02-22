from collections import defaultdict
from typing import Optional, List
from utils import TreeNode


class Solution:
    def compute(self, placement, level, root, dic):
        if not root:
            return
        dic[placement].append((level, root.val))
        self.compute(placement - 1, level + 1, root.left, dic)
        self.compute(placement + 1, level + 1, root.right, dic)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        self.compute(0, 0, root, dic)
        result = []
        for i in sorted(dic.keys()):
            tmp = []
            for j in sorted(dic[i]):
                tmp.append(j[1])
            result.append(tmp)
        return result


s = Solution()
t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.verticalTraversal(t))
