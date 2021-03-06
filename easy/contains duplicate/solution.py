from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate1(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(0, n - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


s = Solution()

print(s.containsDuplicate([1, 2, 3, 1]))
print(s.containsDuplicate([1, 2, 3, 4]))
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
