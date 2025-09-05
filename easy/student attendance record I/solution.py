class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for ch in s:
            if ch == 'A':
                a += 1
                if a >= 2:
                    return False
                l = 0
            elif ch == 'L':
                l += 1
                if l >= 3:
                    return False
            else:
                l = 0

        return True


s = Solution()

print(s.checkRecord("PPALLP"))
print(s.checkRecord("PPALLL"))
