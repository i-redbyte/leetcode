from typing import Optional, List
from utils import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lvls = []

        def bfs(node, level):
            if node:
                if len(lvls) == level:
                    lvls.append([])
                lvls[level] += [node.val]
                bfs(node.left, level + 1)
                bfs(node.right, level + 1)

        bfs(root, 0)
        result = []
        for i in lvls:
            result.append((sum(i)) / len(i))
        return result


t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().averageOfLevels(t))
