class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        n = len(s)
        cycl = 2 * numRows - 2
        for i in range(numRows):
            j = 0
            while j + i < n:
                result += s[i + j]
                if i != 0 and i != numRows - 1 and j + cycl - i < n:
                    result += s[j + cycl - i]
                j += cycl
        return result


s = Solution()

print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
print(s.convert("A", 1))
print(s.convert("", 3))
