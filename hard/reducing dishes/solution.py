from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        result, s = 0, 0
        n = len(satisfaction) - 1
        for i in range(n, -1, -1):
            s += satisfaction[i]
            if s > 0:
                result += s
            else:
                break
        return result


s = Solution()
print(s.maxSatisfaction([-1, -8, 0, 5, -9]))
print(s.maxSatisfaction([4, 3, 2]))
print(s.maxSatisfaction([-1, -4, -5]))
print(s.maxSatisfaction([-2, 5, -1, 0, 3, -3]))
