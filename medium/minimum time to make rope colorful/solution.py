from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        prev_time = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                result += min(prev_time, neededTime[i])
                prev_time = max(prev_time, neededTime[i])
            else:
                prev_time = neededTime[i]

        return result

s = Solution()
print(s.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))
print(s.minCost(colors="abc", neededTime=[1, 2, 3]))
print(s.minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]))
