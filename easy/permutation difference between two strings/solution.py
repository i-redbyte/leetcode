from collections import defaultdict


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        n = len(s)
        sd = defaultdict(int)
        td = defaultdict(int)
        for i in range(n):
            sd[s[i]] = i
            td[t[i]] = i
        for key in sd:
            result += abs(sd[key] - td[key])
        return result


s = Solution()
print(s.findPermutationDifference(s="abc", t="bac"))
print(s.findPermutationDifference(s="abcde", t="edbac"))
