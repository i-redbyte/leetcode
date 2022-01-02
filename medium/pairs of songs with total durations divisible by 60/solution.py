from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result = 0
        count = [0] * 60
        n = len(time)
        for i in range(n):
            pos = time[i] % 60
            result += count[(60 - pos) % 60]
            count[pos] += 1
        return result


s = Solution()
print(s.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
print(s.numPairsDivisibleBy60([60, 60, 60]))
