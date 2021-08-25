from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result = 0
        n = len(heights)
        sort_heights = sorted(heights)
        for i in range(0, n):
            if sort_heights[i] != heights[i]:
                result += 1
        return result


s = Solution()
print(s.heightChecker([1, 1, 4, 2, 1, 3]))
print(s.heightChecker([5, 1, 2, 3, 4]))
print(s.heightChecker([1, 2, 3, 4, 5]))
print(s.heightChecker([1]))
print(s.heightChecker([]))
