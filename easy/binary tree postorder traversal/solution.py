from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [(False, root)]
        while stack:
            flag, val = stack.pop()
            if val:
                if not flag:
                    stack.append((True, val))
                    stack.append((False, val.right))
                    stack.append((False, val.left))
                else:
                    result.append(val.val)
        return result

    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


s = Solution()
t1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(s.postorderTraversal(t1))
