import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        n = len(c.values())
        m = len(set(c.values()))
        return n == m


s = Solution()
print(s.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(s.uniqueOccurrences([1, 2]))
print(s.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
