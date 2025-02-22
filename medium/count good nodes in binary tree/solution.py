from utils import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            result = 0
            if node.val >= max_val:
                result = 1
            max_val = max(max_val, node.val)
            return result + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, -99999999)


s = Solution()
t = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
print(s.goodNodes(t))
