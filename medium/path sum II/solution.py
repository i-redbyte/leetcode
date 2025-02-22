from typing import List
from utils import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.result = []
        self.dfs(root, targetSum, 0, [])
        return self.result

    def dfs(self, root: TreeNode, target: int, prev_sum: int, resultList: list):
        if not root:
            return
        prev_sum += root.val
        resultList.append(root.val)

        if prev_sum == target and root.left is None and root.right is None:
            self.result.append(resultList[:])

        self.dfs(root.left, target, prev_sum, resultList)
        self.dfs(root.right, target, prev_sum, resultList)
        resultList.pop()


s = Solution()

tree1 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), ),
                 TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(1))))
print(s.pathSum(tree1, 22))

tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.pathSum(tree2, 5))

tree3 = TreeNode(1, TreeNode(2))
print(s.pathSum(tree3, 0))
