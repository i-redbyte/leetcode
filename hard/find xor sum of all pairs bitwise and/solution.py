from functools import reduce
from operator import xor
from typing import List


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        return reduce(xor, arr1) & reduce(xor, arr2)

    def getXORSum1(self, arr1: List[int], arr2: List[int]) -> int:
        a = arr1[0]
        b = arr2[0]
        n = len(arr1)
        m = len(arr2)
        for i in range(1, n):
            a = a ^ arr1[i]
        for j in range(1, m):
            b = b ^ arr2[j]
        return a & b


print(Solution().getXORSum(arr1=[1, 2, 3], arr2=[6, 5]))
print(Solution().getXORSum(arr1=[12], arr2=[4]))
