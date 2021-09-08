from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        nums1 = nums[1:]
        nums2 = nums[:len(nums) - 1]
        prev1 = 0
        cur1 = nums1[0]
        prev2 = 0
        cur2 = nums2[0]
        n = len(nums1) + 1
        for i in range(2, n):
            tmp = cur1
            cur1 = max(prev1 + nums1[i - 1], cur1)
            prev1 = tmp
            tmp = cur2
            cur2 = max(prev2 + nums2[i - 1], cur2)
            prev2 = tmp
        return max(cur1, cur2)


s = Solution()
print(s.rob([2, 3, 2]))
print(s.rob([1, 2, 3, 1]))
print(s.rob([1, 2, 3]))
