# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
import random


class Solution:
    def guessNumber(self, n: int) -> int:
        # FROM TEST
        # pick = random.randrange(n + 1)
        #
        # def guess(num: int) -> int:
        #     if num > pick:
        #         return -1
        #     if num < pick:
        #         return 1
        #     return 0
        left = 0
        right = n
        mid = (left + right) // 2
        g = guess(mid)
        while g != 0 and left < right:
            if g == 1:
                left = mid + 1
                mid = (left + right) // 2
                g = guess(mid)
            else:
                right = mid - 1
                mid = (left + right) // 2
                g = guess(mid)
        return mid


s = Solution()
print("Result:")
print(s.guessNumber(n=10))
print(s.guessNumber(n=1))
print(s.guessNumber(n=2))
