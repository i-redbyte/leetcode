from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n_bytes = 0
        seven_bit = 1 << 7
        six_bit = 1 << 6
        for num in data:
            mask = 1 << 7
            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1
                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if not (num & seven_bit and not (num & six_bit)):
                    return False
            n_bytes -= 1
        return n_bytes == 0


s = Solution()
print(s.validUtf8([197, 130, 1]))
print(s.validUtf8([235, 140, 4]))
