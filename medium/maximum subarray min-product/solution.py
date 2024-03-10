from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        d = int(1e9 + 7)
        result, s = 0, 0
        nums.append(0)
        stack = []
        for i, v in enumerate(nums):
            while stack and nums[stack[-1][0]] >= v:
                index, _ = stack.pop()
                tmp = s
                if stack:
                    tmp = s - stack[-1][1]
                result = max(result, nums[index] * tmp)
            s += v
            stack.append((i, s))
        return result % d


s = Solution()
print(s.maxSumMinProduct([1, 2, 3, 2]))
print(s.maxSumMinProduct([2, 3, 3, 1, 2]))
print(s.maxSumMinProduct([3, 1, 5, 6, 4, 2]))
