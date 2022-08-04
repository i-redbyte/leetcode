from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        result = -1
        for i in arr:
            if d[i] == i:
                result = max(result, i)
        return result

    def findLucky1(self, arr: List[int]) -> int:
        d = dict()
        n = len(arr) - 1
        arr.sort(reverse=True)
        for i in arr:
            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1
        for i in arr:
            if d[i] == i:
                return i
        return -1


s = Solution()
print(s.findLucky([2, 2, 3, 4]))
print(s.findLucky([1, 2, 2, 3, 3, 3]))
print(s.findLucky([2, 2, 2, 3, 3]))
