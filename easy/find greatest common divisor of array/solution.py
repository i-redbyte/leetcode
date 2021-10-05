from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_number = max(nums)
        min_number = min(nums)
        k = 1
        result = 0
        while max_number != 0 and min_number != 0:
            while max_number % 2 == 0 and min_number % 2 == 0:
                max_number = max_number // 2
                min_number = min_number // 2
                k *= 2
            while max_number % 2 == 0:
                max_number = max_number // 2
            while min_number % 2 == 0:
                min_number = min_number // 2
            if max_number >= min_number:
                max_number = max_number - min_number
            else:
                min_number = min_number - max_number
            result = min_number * k
        return result

    def findGCD1(self, nums: List[int]) -> int:
        max_number = max(nums)
        min_number = min(nums)
        for i in range(min_number, 0, -1):
            if max_number % i == 0 and min_number % i == 0:
                return i
        return 0


s = Solution()
print(s.findGCD([2, 5, 6, 9, 10]))
print(s.findGCD([7, 5, 6, 8, 3]))
print(s.findGCD([3, 3]))
print(s.findGCD([5, 6, 15]))
