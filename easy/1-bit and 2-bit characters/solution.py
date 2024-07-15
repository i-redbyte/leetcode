from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        def canDecode(index: int) -> bool:
            if index >= len(bits):
                return False
            if index == len(bits) - 1:
                return True
            if bits[index] == 0:
                return canDecode(index + 1)
            elif bits[index] == 1:
                return canDecode(index + 2)
            return False
        return canDecode(0)

    def isOneBitCharacter2(self, bits: List[int]) -> bool:
        n = len(bits)
        i = n - 2
        while i >= 0 and bits[i] > 0:
            i -= 1
        return (n - i) % 2 == 0

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
