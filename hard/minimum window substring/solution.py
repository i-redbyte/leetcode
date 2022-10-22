import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        m = len(t)
        i = k = h = 0
        for j, c in enumerate(s, 1):
            m -= need[c] > 0
            need[c] -= 1
            if not m:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not h or j - i <= h - k:
                    k, h = i, j
        return s[k:h]


s = Solution()
print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
print(s.minWindow(s="a", t="a"))
print(s.minWindow(s="a", t="aa"))
