from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        level = [0] * n
        tree = defaultdict(list)
        for left, right in edges:
            tree[left].append(right)
            tree[right].append(left)
            level[left] += 1
            level[right] += 1
        border = [i for i in range(n) if level[i] == 1]

        while border:
            nxt_step = []
            for n in border:
                for nx in tree[n]:
                    level[nx] -= 1
                    if level[nx] == 1:
                        nxt_step.append(nx)
            if not nxt_step:
                return border
            border = nxt_step


s = Solution()

print(s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
