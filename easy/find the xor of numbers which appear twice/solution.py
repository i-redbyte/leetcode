from collections import defaultdict
from functools import reduce
from itertools import chain
from operator import xor
from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        result = 0
        for num, count in d.items():
            if count == 2:
                result ^= num

        return result

    def duplicateNumbersXOR2(self, nums: List[int]) -> int:
        return reduce(xor, chain(nums, set(nums)))

    def duplicateNumbersXOR1(self, nums: List[int]) -> int:
        result = 0
        s = set()
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    s.add(nums[i])
        if len(s) == 0:
            return result
        for i in s:
            result = result ^ i
        return result


s = Solution()
print(s.duplicateNumbersXOR([1, 2, 1, 3]))
print(s.duplicateNumbersXOR([1, 2, 3]))
print(s.duplicateNumbersXOR([1, 2, 2, 1]))
