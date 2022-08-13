from collections import defaultdict
from typing import List


class Solution:
    def findShortestSubArray(self, nums):
        dick = {}
        tmp = 1
        result = 1
        for i, x in enumerate(nums):
            if x in dick:
                dick[x][1] += 1
                m = dick[x][1]
                length = i - dick[x][0] + 1
            else:
                dick[x] = [i, 1]
                length = m = 1
            if m > tmp:
                tmp, result = m, length
            elif tmp == m:
                result = min(result, length)
        return result

    def findShortestSubArray1(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        m = max([len(v) for v in d.values()])
        result = len(nums)
        for v in d.values():
            if len(v) == m:
                result = min(result, v[-1] - v[0] + 1)
        return result


s = Solution()
print(s.findShortestSubArray([1, 2, 2, 3, 1]))
print(s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
