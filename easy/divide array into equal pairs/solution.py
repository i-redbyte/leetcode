from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        for i in range(0, n, 2):
            if (nums[i] ^ nums[i + 1]) != 0:
                return False
        return True

    def divideArray1(self, nums: List[int]) -> bool:
        dick = {}
        for n in nums:
            if n in dick:
                dick[n] += 1
            else:
                dick[n] = 1
        for v in dick.values():
            if v & 1 != 0:
                return False
        return True


s = Solution()
print(s.divideArray([3, 2, 3, 2, 2, 2]))
print(s.divideArray([1, 2, 3, 4]))
print(s.divideArray([9, 4, 18, 3, 2, 6, 18, 15, 7, 15, 6, 4, 15, 14, 7, 4, 15, 4, 3, 17, 9, 13, 13, 12, 2, 14, 12, 17]))
