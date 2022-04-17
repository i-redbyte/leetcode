
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_tree = TreeNode()

        def inorder(root, new_tree):
            if not root:
                return
            inorder(root.right, new_tree)
            new_tree.right = TreeNode(root.val, right=new_tree.right)
            inorder(root.left, new_tree)
            new_tree.left = TreeNode(root.val, right=new_tree.right)

        inorder(root, new_tree)
        return new_tree.right


def printTree(node: TreeNode, level=0):
    if node is not None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.val)
        printTree(node.right, level + 1)


s = Solution()
testTree = TreeNode(5, TreeNode(1), TreeNode(7))
printTree(testTree)
printTree(s.increasingBST(testTree))
