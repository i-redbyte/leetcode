from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            nums[abs(i) - 1] = -abs(nums[abs(i) - 1])
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))

    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums) + 1
        s = set(nums)
        for i in range(1, n):
            if i not in s:
                result.append(i)
        return result


s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(s.findDisappearedNumbers([1, 1]))
