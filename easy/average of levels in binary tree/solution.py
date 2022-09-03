from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
