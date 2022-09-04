from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cs = Counter(s)
        flag = False
        result = 0
        for ch in cs:
            val = cs[ch]
            if val % 2 == 0:
                result += val
            else:
                if flag:
                    result += val - 1
                else:
                    result += val
                    flag = True
        return result


s = Solution()
print(s.longestPalindrome("abccccdd"))
print(s.longestPalindrome("a"))
