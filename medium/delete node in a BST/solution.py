# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()


class Solution:
    def min_value(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left:
            current = current.left
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.left and root.right:
                return root.right
            if root.left and not root.right:
                return root.left
            if root.left and root.right:
                tmp = self.min_value(root.right)
                root.val = tmp.val
                root.right = self.deleteNode(root.right, root.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def deleteNode1(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            t = TreeNode()
            if not root.left:
                t = root.right
                root.right = None
                return t
            elif not root.right:
                t = root.left
                root.left = None
                return t
            else:
                t = self.min_value(root.right)
                root.val = t.val
                root.right = self.deleteNode(root.right, t.val)
        return root


def printTree(node: TreeNode, level=0):
    if node is not None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.val)
        printTree(node.right, level + 1)


s = Solution()
tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
print("After:")
printTree(tree)
print("Before:")
printTree(s.deleteNode(tree, 3))

