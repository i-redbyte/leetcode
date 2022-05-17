import math


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 26
        result = 0
        alphabet = {
            "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
            "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16,
            "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
            "X": 24, "Y": 25, "Z": 26
        }
        reverse_title = reversed(columnTitle)
        for i, ch in enumerate(reverse_title):
            result += alphabet[ch] * int(math.pow(base, i))
        return result


s = Solution()
print(s.titleToNumber("A"))
print(s.titleToNumber("AB"))
print(s.titleToNumber("ZY"))
