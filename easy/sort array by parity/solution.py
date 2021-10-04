from typing import List


class Solution:

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, k = 0, len(nums) - 1
        while i < k:
            if nums[i] & 1 > nums[k] & 1:
                nums[i], nums[k] = nums[k], nums[i]
            if nums[i] & 1 == 0:
                i += 1
            if nums[k] & 1 == 1:
                k -= 1
        return nums

    def sortArrayByParity1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in nums:
            if i & 1 == 0:
                result.insert(0, i)
            else:
                result.insert(n, i)
        return result


s = Solution()
print(s.sortArrayByParity([3, 1, 2, 4]))
print(s.sortArrayByParity([0]))
