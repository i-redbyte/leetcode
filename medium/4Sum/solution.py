from typing import List


class Solution:
    def k_sum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        result = []
        if not nums:
            return result
        average_value = target // k

        if average_value < nums[0] or nums[-1] < average_value:
            return result
        if k == 2:
            return self.two_sum(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for subset in self.k_sum(nums[i + 1:], target - nums[i], k - 1):
                    result.append([nums[i]] + subset)

        return result

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[List[int]]:
        result = []
        s = set()
        for i in range(len(nums)):
            if len(result) == 0 or result[-1][1] != nums[i]:
                if target - nums[i] in s:
                    result.append([target - nums[i], nums[i]])
            s.add(nums[i])
        return result

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.k_sum(nums, target, 4)


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s.fourSum([2, 2, 2, 2, 2], 8))
