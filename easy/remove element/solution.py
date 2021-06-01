from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = nums.count(val)
        x = 0
        n = len(nums)
        for i in range(counter):
            pos = nums.index(val)
            if nums.pop(pos):
                x += 1
        return n - x


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
