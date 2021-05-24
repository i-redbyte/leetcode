from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        while n >= 0:
            if digits[n] == 9:
                digits[n] = 0
            else:
                digits[n] += 1
                return digits
            n = n - 1
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


s = Solution()
print(s.plusOne([9, 9, 9]))
print(s.plusOne([9, 8, 9]))
print(s.plusOne([1, 2, 3]))
print(s.plusOne([4, 3, 2, 1]))
print(s.plusOne([0]))
print(s.plusOne([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))
