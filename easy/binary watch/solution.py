from typing import List


class Solution:
    def bit_counter(self, n: int) -> int:
        result = 0
        while n != 0:
            if n & 1 == 1:
                result += 1
            n >>= 1
        return result

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(12):
            for m in range(60):
                if self.bit_counter(h) + self.bit_counter(m) == turnedOn:
                    result.append(f'{h}:{m:02}')
        return result


s = Solution()
print(s.readBinaryWatch(9))
print(s.readBinaryWatch(0))
print(s.readBinaryWatch(7))
print(s.readBinaryWatch(1))
