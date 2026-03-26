from typing import List
from collections import defaultdict


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(g: List[List[int]]) -> bool:
            m, n = len(g), len(g[0])

            top_sum = 0
            bottom_sum = 0

            top_cnt = defaultdict(int)
            bottom_cnt = defaultdict(int)

            for row in g:
                for x in row:
                    bottom_sum += x
                    bottom_cnt[x] += 1

            for i in range(m - 1):
                for x in g[i]:
                    top_sum += x
                    bottom_sum -= x
                    top_cnt[x] += 1
                    bottom_cnt[x] -= 1

                if top_sum == bottom_sum:
                    return True

                if top_sum < bottom_sum:
                    diff = bottom_sum - top_sum
                    if bottom_cnt[diff] > 0:
                        if (
                                (m - i - 1 > 1 and n > 1)
                                or (i == m - 2 and (g[i + 1][0] == diff or g[i + 1][-1] == diff))
                                or (n == 1 and (g[i + 1][0] == diff or g[-1][0] == diff))
                        ):
                            return True
                else:
                    diff = top_sum - bottom_sum
                    if top_cnt[diff] > 0:
                        if (
                                (i + 1 > 1 and n > 1)
                                or (i == 0 and (g[0][0] == diff or g[0][-1] == diff))
                                or (n == 1 and (g[0][0] == diff or g[i][0] == diff))
                        ):
                            return True

            return False

        return check(grid) or check([list(row) for row in zip(*grid)])


s = Solution()
print(s.canPartitionGrid(grid=[[1, 4], [2, 3]]))
print(s.canPartitionGrid(grid=[[1, 2], [3, 4]]))
print(s.canPartitionGrid(grid=[[1, 2, 4], [2, 3, 5]]))
