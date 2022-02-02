from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n_p = len(p)
        n_s = len(s)
        if n_p > len(s):
            return []
        delta = [0] * 26  # 26 - alphabet symbols
        mask = [0] * 26
        result = []
        for i in range(n_p):
            delta[ord(p[i]) - 97] += 1
            mask[ord(s[i]) - 97] += 1
        if mask == delta:
            result.append(0)
        for i in range(n_p, n_s):
            mask[ord(s[i - n_p]) - 97] -= 1
            mask[ord(s[i]) - 97] += 1
            if mask == delta:
                result.append(i - n_p + 1)
        return result


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))
