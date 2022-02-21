from typing import List


class Solution:
    # Boyer-Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

    def majorityElement1(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) < 3:
            return max(nums)
        half = n // 2
        nums.sort()
        return nums[half]


print(Solution().majorityElement([3, 2, 3]))
print(Solution().majorityElement([3, 3, 4]))
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(Solution().majorityElement([6,5,5]))
