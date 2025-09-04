class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return max(len(a), len(b))


s = Solution()
print(s.findLUSlength("aba", "cdc"))
print(s.findLUSlength("aaa", "bbb"))
print(s.findLUSlength("aaa", "aaa"))
print(s.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))
