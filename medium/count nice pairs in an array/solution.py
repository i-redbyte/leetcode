import collections
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        result = 0
        h = collections.defaultdict(int)
        for i in range(len(nums)):
            k = self.rev(nums[i]) - nums[i]
            if k in h:
                result += h[k]
            h[k] += 1
        return result % (10 ** 9 + 7)

    def rev(self, num: int) -> int:
        x = num
        res = 0
        while x > 0:
            pop = x % 10
            res = 10 * res + pop
            x = x // 10
        return res

    def countNicePairs2(self, nums: List[int]) -> int:
        mydict = collections.defaultdict(list)
        count = 0
        for i in range(len(nums)):
            lhs = nums[i] - int(str(nums[i])[::-1])
            if lhs in mydict:
                count += len(mydict[lhs])
            mydict[lhs].append(i)
        return count % (10 ** 9 + 7)


s = Solution()
print(s.countNicePairs([42, 11, 1, 97]))
print(s.countNicePairs([13, 10, 35, 24, 76]))
