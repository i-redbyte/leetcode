# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printTree(node: 'TreeNode', level=0):
    if node is not None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.val)
        printTree(node.right, level + 1)
