class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        l = list(s)
        n = len(s) // 2
        while left <= n:
            l[left] = min(l[left], l[right])
            l[right] = l[left]
            left += 1
            right -= 1
        return "".join(l)


s = Solution()
print(s.makeSmallestPalindrome("egcfe"))
print(s.makeSmallestPalindrome("abcd"))
print(s.makeSmallestPalindrome("seven"))
