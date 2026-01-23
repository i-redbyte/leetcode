from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        w = widths
        cur = 0
        lines = 1
        base = ord('a')

        for ch in s:
            x = w[ord(ch) - base]
            nx = cur + x
            if nx > 100:
                lines += 1
                cur = x
            else:
                cur = nx

        return [lines, cur]


s = Solution()
print(s.numberOfLines(
    widths=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="abcdefghijklmnopqrstuvwxyz"))
print(s.numberOfLines(
    widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="bbbcccdddaaa"))
