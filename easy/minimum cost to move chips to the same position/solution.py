from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counts = [0, 0]
        for i in position:
            counts[i & 1] += 1
        return min(counts)

    def minCostToMoveChips1(self, position: List[int]) -> int:
        even_step_counter = 0
        odd_step_counter = 0
        for i in position:
            if i & 1 == 0:
                even_step_counter += 1
            else:
                odd_step_counter += 1
        return min(even_step_counter, odd_step_counter)


s = Solution()
print(s.minCostToMoveChips([1, 2, 3]))
print(s.minCostToMoveChips([2, 2, 2, 3, 3]))
print(s.minCostToMoveChips([1, 1000000000]))
