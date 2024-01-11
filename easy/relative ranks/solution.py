from collections import defaultdict
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = []
        d = defaultdict(str)
        sort_score = sorted(score, reverse=True)

        for i, v in enumerate(sort_score):
            if i == 0:
                d[v] = "Gold Medal"
            elif i == 1:
                d[v] = "Silver Medal"
            elif i == 2:
                d[v] = "Bronze Medal"
            else:
                d[v] = str(i + 1)
        for i in score:
            result.append(d[i])
        return result


print(Solution().findRelativeRanks([5, 4, 3, 2, 1]))
print(Solution().findRelativeRanks([10, 3, 8, 9, 4]))
print(Solution().findRelativeRanks([1]))
