class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = ''
        if numerator * denominator < 0:
            sign = '-'
        result = [sign + str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(n))

        i = stack.index(remainder)
        result.insert(i + 2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')


s = Solution()
print(s.fractionToDecimal(1, 2))
print(s.fractionToDecimal(2, 1))
print(s.fractionToDecimal(4, 333))
