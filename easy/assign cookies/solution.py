from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        n = len(g)
        m = len(s)
        while i < n and j < m:
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i


s = Solution()
print(s.findContentChildren([1, 2, 3], s=[1, 1]))
print(s.findContentChildren(g=[1, 2], s=[1, 2, 3]))
