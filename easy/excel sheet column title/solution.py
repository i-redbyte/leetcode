class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet_len = 26
        alphabet = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
                    13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W',
                    24: 'X', 25: 'Y', 26: 'Z'}
        result = ""
        while columnNumber > alphabet_len:
            if columnNumber % alphabet_len != 0:
                result += alphabet[columnNumber % alphabet_len]
                columnNumber //= alphabet_len
            else:
                result += alphabet[alphabet_len]
                columnNumber = columnNumber // alphabet_len - 1
        result += alphabet[columnNumber]
        return result[::-1]


print(Solution().convertToTitle(1))
print(Solution().convertToTitle(28))
print(Solution().convertToTitle(701))
