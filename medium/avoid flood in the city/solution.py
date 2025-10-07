from typing import List
from bisect import bisect_right, insort


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        result = [-1] * n
        last = {}
        dry_days = []

        for i, x in enumerate(rains):
            if x > 0:
                if x in last:
                    pos = bisect_right(dry_days, last[x])
                    if pos == len(dry_days):
                        return []
                    dry_idx = dry_days.pop(pos)
                    result[dry_idx] = x
                last[x] = i
                result[i] = -1
            else:
                result[i] = 1
                insort(dry_days, i)

        return result


s = Solution()
print(s.avoidFlood([1, 2, 3, 4]))
print(s.avoidFlood([1, 2, 0, 0, 2, 1]))
print(s.avoidFlood([1, 2, 0, 1, 2]))
