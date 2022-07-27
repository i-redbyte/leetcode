from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(nums[i])
        return ans


s = Solution()
print(s.buildArray(nums=[0, 2, 1, 5, 3, 4]))
print(s.buildArray([5, 0, 1, 2, 3, 4]))
