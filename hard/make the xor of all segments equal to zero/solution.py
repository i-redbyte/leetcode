from collections import Counter
from itertools import accumulate
from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        maxNum = 1 << 10

        n = len(nums)
        mins = [(n - j + k - 1) // k for j in range(k)]
        counts = [Counter(nums[j::k]).most_common() for j in range(k)]

        last = counts[-1]
        tmp = mins[-1]
        dp = [tmp] * maxNum
        for j, v in last:
            dp[j] -= v

        for itNum in range(k - 2, -1, -1):
            here = mins[itNum]
            minCost = min(dp)
            newDP = [minCost + here] * maxNum

            for j, v in counts[itNum]:
                newAdd = here - v
                for currX in range(maxNum):
                    newDP[currX] = min(newDP[currX], newAdd + dp[j ^ currX])
            dp = newDP[:]
        return dp[0]


s = Solution()
print(s.minChanges(nums=[1, 2, 0, 3, 0], k=1))
print(s.minChanges(nums=[3, 4, 5, 2, 1, 7, 3, 4, 7], k=3))
print(s.minChanges(nums=[1, 2, 4, 1, 2, 5, 1, 2, 6], k=3))
