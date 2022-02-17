from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        universe = [([], 0)]
        for number in candidates:
            for (ls, val) in universe:
                if val + number == target:
                    result.append(ls + [number])
                elif val + number < target:
                    universe.append((ls + [number], val + number))
        return result


print(Solution().combinationSum([2, 3, 6, 7], 7))
print(Solution().combinationSum([2, 3, 5], 8))
print(Solution().combinationSum([2], 1))
