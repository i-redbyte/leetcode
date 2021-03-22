class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if 10 > x:
            return True
        result: int = 0
        tmp = x
        while x > 0:
            y = x % 10
            result = (result * 10) + y
            x = int(x / 10)
        return result == tmp


s = Solution()
print(s.isPalindrome(10))
print(s.isPalindrome(101))
print(s.isPalindrome(-101))
print(s.isPalindrome(222))
print(s.isPalindrome(506))
print(s.isPalindrome(10001))
