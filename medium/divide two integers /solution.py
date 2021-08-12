class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0):
            sign = -1
        check_size = 1 << 31
        if sign >= 0:
            check_size = (1 << 31) - 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        dividend = [int(x) for x in bin(dividend)[2:]]
        cur_div = 0
        result = 0
        for next_digit in dividend:
            cur_div = (cur_div << 1) + next_digit
            if divisor <= cur_div:
                cur_div -= divisor
                new_digit = 1
            else:
                new_digit = 0
            result = (result << 1) + new_digit
        result = min(result, check_size)
        if sign < 0:
            result = - result
        return result

    # first fast solution
    def divide_slow(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            dividend -= divisor
            result += 1
        if sign < 0:
            result = -result
        return result


s = Solution()
print(s.divide(10, 3))
print(s.divide(7, -3))
print(s.divide(0, 1))
print(s.divide(1, 1))
print(s.divide(5, 1))
print(s.divide(-2147483648, -1))
