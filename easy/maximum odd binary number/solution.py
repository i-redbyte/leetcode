class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "1" * (n1 := s.count('1') - 1) + "0" * (len(s) - n1 - 1) + "1"

    def maximumOddBinaryNumber2(self, s: str) -> str:
        sorts = sorted(s, reverse=True)
        n = len(s)
        for i in range(n - 1, -1, -1):
            if sorts[i] == '1':
                sorts[i], sorts[-1] = sorts[-1], sorts[i]
                break
        return ''.join(sorts)

    def maximumOddBinaryNumber1(self, s: str) -> str:
        n = len(s)
        ones = 0
        for ch in s:
            if ch == "1":
                ones += 1
        result = ['0'] * (n - 1) + ['1']
        if ones == 1:
            return "".join(result)
        for i in range(0, ones - 1):
            result[i] = "1"
        return "".join(result)


s = Solution()
print(s.maximumOddBinaryNumber("010"))
print(s.maximumOddBinaryNumber("0101"))
