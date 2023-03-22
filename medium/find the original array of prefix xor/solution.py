from functools import reduce
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        result = []
        v = 0
        for i in pref:
            result.append(i ^ v)
            v ^= result[len(result)-1]
        return result

    def findArray1(self, pref: List[int]) -> List[int]:
        n = len(pref)
        result = [pref[0]]
        for i in range(1, n):
            v = reduce(lambda a, b: a ^ b, result) ^ pref[i]
            result.append(v)
        return result


s = Solution()
print(s.findArray([5, 2, 0, 3, 1]))
print(s.findArray([13]))
