from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = [True] * n
        m = max(candies)
        half = n // 2 + 1
        for i in range(half):
            if candies[i] + extraCandies < m:
                result[i] = False
            if candies[n - i - 1] + extraCandies < m:
                result[n - i - 1] = False
        return result


s = Solution()
print(s.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
print(s.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
print(s.kidsWithCandies(candies=[12, 1, 12], extraCandies=10))
