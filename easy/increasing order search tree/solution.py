from utils import TreeNode, printTree


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


s = Solution()
testTree = TreeNode(5, TreeNode(1), TreeNode(7))
printTree(testTree)
printTree(s.increasingBST(testTree))
