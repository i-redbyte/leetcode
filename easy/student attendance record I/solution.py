class Solution:
    def checkRecord(self, s: str) -> bool:
        state = 0  # bits 0-1: counter A, bits 2-3: counter L
        for char in s:
            if char == 'A':
                a_count = (state & 0b11) + 1
                if a_count > 2:
                    a_count = 2
                state = (state & 0b11111100) | a_count
                state &= 0b00000011

            elif char == 'L':
                l_count = ((state >> 2) & 0b11) + 1
                if l_count > 3:
                    l_count = 3
                state = (state & 0b11110011) | (l_count << 2)

            else:  # 'P'
                state &= 0b00000011

            if (state & 0b11) >= 2:
                return False
            if ((state >> 2) & 0b11) >= 3:
                return False

        return True

    def checkRecord1(self, s: str) -> bool:
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
print(s.checkRecord("AAAA"))
