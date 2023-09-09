class Solution:
    def splitNum(self, num: int) -> int:
        s = sorted(str(num))
        return int("".join(s[::2])) + int("".join(s[1::2]))


s = Solution()
print(s.splitNum(4325))
print(s.splitNum(687))
