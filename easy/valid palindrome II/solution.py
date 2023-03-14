class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        lo = 0
        hi = n - 1
        deleted = False
        temp_lo = lo
        temp_hi = hi
        exist_temp = False
        while lo < hi:
            if s[lo] != s[hi]:
                if not deleted:
                    deleted = True
                    temp_lo = lo
                    temp_hi = hi - 1
                    exist_temp = True
                    lo += 1
                    continue
                elif exist_temp:
                    lo = temp_lo
                    hi = temp_hi
                    exist_temp = False
                    continue
                else:
                    return False
            lo += 1
            hi -= 1
        return True


s = Solution()
print(s.validPalindrome("aba"))
print(s.validPalindrome("abca"))
print(s.validPalindrome("abc"))
