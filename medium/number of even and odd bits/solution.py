from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        result = [0] * 2
        cnt = 0
        while n:
            result[cnt & 1] += n & 1
            cnt += 1
            n >>= 1
        return result

    def evenOddBit2(self, n: int) -> List[int]:
        return [(n & 0b10101010101).bit_count(), (n & 0b01010101010).bit_count()]

    def evenOddBit1(self, n: int) -> List[int]:
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
print(s.evenOddBit(111))
