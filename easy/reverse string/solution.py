"""
    Do not return anything, modify s in-place instead.
"""
from typing import List


class Solution:
    def reverseString2(self, s: List[str]) -> None:
        s[::-1] = s  # or s.reverse()
        print(s)
        return

    def reverseString(self, s: List[str]) -> None:
        n = len(s) - 1
        h = len(s) // 2
        for i in range(0, h):
            tmp = s[i]
            s[i] = s[n - i]
            s[n - i] = tmp
        print(s)
        return


s = Solution()
s.reverseString(["h", "e", "l", "l", "o"])
s.reverseString(["H", "a", "n", "n", "a", "h"])
s.reverseString(["+", "+", "C"])
s.reverseString([""])
s.reverseString(["1"])
s.reverseString(["1", "2"])
