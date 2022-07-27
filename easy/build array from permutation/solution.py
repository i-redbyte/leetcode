from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]

    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i, v in enumerate(nums):
            nums[i] += n * (nums[v] % n)
        for i in range(n):
            nums[i] //= n
        return nums

    def buildArray1(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(nums[i])
        return ans


s = Solution()
# print(s.buildArray(nums=[0, 2, 1, 5, 3, 4]))
print(s.buildArray([5, 0, 1, 2, 3, 4]))
