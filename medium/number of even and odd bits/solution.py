from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even_count = 0
        odd_count = 0
        while n != 0:
            if n & 1:
                even_count += 1
            n = n >> 1
            if n != 0 and n & 1:
                odd_count += 1
            n = n >> 1
        return [even_count, odd_count]


s = Solution()
print(s.evenOddBit(17))
print(s.evenOddBit(2))
