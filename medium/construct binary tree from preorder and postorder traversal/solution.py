from typing import List, Optional
from utils import TreeNode, printTree


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_idx_map = {val: idx for idx, val in enumerate(postorder)}

        def build(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end or post_start > post_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            if pre_start == pre_end:
                return root

            left_root_val = preorder[pre_start + 1]
            left_root_post_idx = post_idx_map[left_root_val]
            left_size = left_root_post_idx - post_start + 1

            root.left = build(pre_start + 1, pre_start + left_size, post_start, left_root_post_idx)
            root.right = build(pre_start + left_size + 1, pre_end, left_root_post_idx + 1, post_end - 1)

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)


s = Solution()
preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]
printTree(s.constructFromPrePost(preorder, postorder))
