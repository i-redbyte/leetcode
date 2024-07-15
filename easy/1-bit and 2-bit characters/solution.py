from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = len(bits) - 2
        while i >= 0 and bits[i] > 0:
            i -= 1
        return (len(bits) - i) % 2 == 0

    def isOneBitCharacter1(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1


s = Solution()
print(s.isOneBitCharacter([1, 0, 0]))
print(s.isOneBitCharacter([1, 1, 1, 0]))
