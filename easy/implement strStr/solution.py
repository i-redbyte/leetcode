from pip._vendor.msgpack.fallback import xrange
# use KMP algorithm
# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        d = self.prefix(needle)
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = d[j - 1]
        else:
            if j == len(needle):
                return i - j
            return -1

    def prefix(self, s):
        dict = {0: 0}
        for i in xrange(1, len(s)):
            j = dict[i - 1]
            while j > 0 and s[j] != s[i]:
                j = dict[j - 1]
            if s[j] == s[i]:
                j += 1
            dict[i] = j
        return dict


s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("aaaaa", "baa"))
print(s.strStr("", ""))
print(s.strStr("lenin & stalin", "in"))
