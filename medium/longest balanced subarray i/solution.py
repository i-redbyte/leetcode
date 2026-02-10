from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            seen = set()
            even = odd = 0
            for j in range(i, n):
                x = nums[j]
                if x not in seen:
                    seen.add(x)
                    if x & 1:
                        odd += 1
                    else:
                        even += 1
                if even == odd:
                    result = max(result, j - i + 1)
        return result


s = Solution()
print(s.longestBalanced([2, 5, 4, 3]))
print(s.longestBalanced([3, 2, 2, 5, 4]))
print(s.longestBalanced([1, 2, 3, 2]))
