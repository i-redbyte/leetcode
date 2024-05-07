from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""

    def firstPalindrome1(self, words: List[str]) -> str:
        def isPalindrome(s: str) -> bool:
            start = 0
            end = len(s) - 1
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        for w in words:
            if isPalindrome(w):
                return w
        return ""


s = Solution()
print(s.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))
print(s.firstPalindrome(["notapalindrome", "racecar"]))
print(s.firstPalindrome(["def", "ghi"]))
