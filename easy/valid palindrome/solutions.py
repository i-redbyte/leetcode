class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_text = ""
        for char in s.lower():
            if ("0" <= char <= "9") or ("a" <= char <= "z"):
                only_text += char
        n = len(only_text) // 2
        text_len = len(only_text) - 1
        for i in range(0, n):
            if only_text[i] != only_text[text_len - i]:
                return False
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome("kazak"))
print(s.isPalindrome("kazzak"))
print(s.isPalindrome("lele"))
