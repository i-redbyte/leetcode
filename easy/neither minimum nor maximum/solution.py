from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        sum = nums[0] + nums[1] + nums[2]
        mx = max(nums[0], nums[1], nums[2])
        mn = min(nums[0], nums[1], nums[2])
        return sum - mx - mn

    def findNonMinOrMax4(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        mid = nums[n // 2]
        first = nums[0]
        last = nums[n - 1]
        sum = first + mid + last
        if (first != mid != last) and (first != last) and (mid != first and mid != last):
            mx = max(first, mid, last)
            mn = min(first, mid, last)
            return sum - mx - mn
        return -1

    def findNonMinOrMax3(self, nums: List[int]) -> int:
        s = set(nums)
        n = len(nums)
        if n < 3:
            return -1
        s.remove(min(s))
        s.remove(max(s))
        return s.pop()

    def findNonMinOrMax2(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        nums.sort()
        mid = nums[n // 2]
        if mid != nums[n - 1] and mid != nums[0]:
            return mid
        return -1

    def findNonMinOrMax1(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        min_el = min(nums)
        max_el = max(nums)
        for x in nums:
            if x != min_el and x != max_el:
                return x
        return -1


s = Solution()
print(s.findNonMinOrMax([3, 2, 1, 4]))
print(s.findNonMinOrMax([1, 2]))
print(s.findNonMinOrMax([2, 1, 3]))
