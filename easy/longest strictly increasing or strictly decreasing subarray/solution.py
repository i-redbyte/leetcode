from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        result = 1
        inc_len = 1
        dec_len = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc_len += 1
                dec_len = 1
            elif nums[i] < nums[i - 1]:
                dec_len += 1
                inc_len = 1
            else:
                inc_len = 1
                dec_len = 1

            result = max(result, inc_len, dec_len)
        return result


s = Solution()
print(s.longestMonotonicSubarray([1, 4, 3, 3, 2]))
print(s.longestMonotonicSubarray([3, 3, 3, 3]))
print(s.longestMonotonicSubarray([3, 2, 1]))
