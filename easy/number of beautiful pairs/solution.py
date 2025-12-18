from typing import List
from math import gcd


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def first_digit(x: int) -> int:
            while x >= 10:
                x //= 10
            return x

        coprime = [[False] * 10 for _ in range(10)]
        for a in range(1, 10):
            for b in range(10):
                coprime[a][b] = (gcd(a, b) == 1)

        cnt_first = [0] * 10
        result = 0

        for x in nums:
            ld = x % 10
            for fd in range(1, 10):
                if coprime[fd][ld]:
                    result += cnt_first[fd]

            cnt_first[first_digit(x)] += 1

        return result


s = Solution()
print(s.countBeautifulPairs([2, 5, 1, 4]))
print(s.countBeautifulPairs([11, 21, 12]))
