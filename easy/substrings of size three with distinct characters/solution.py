class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n - 2):
            s_set = set(s[i:i + 3])
            if len(s_set) == 3:
                result += 1
        return result


s = Solution()
print(s.countGoodSubstrings("xyzzaz"))
print(s.countGoodSubstrings("aababcabc"))
