class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = []
        n = num
        while n > 0:
            digits.append(n % 10)
            n //= 10
        digits.reverse()

        n = len(digits)
        max_idx = [0] * n
        max_idx[-1] = n - 1

        for i in range(n - 2, -1, -1):
            if digits[i] > digits[max_idx[i + 1]]:
                max_idx[i] = i
            else:
                max_idx[i] = max_idx[i + 1]

        for i in range(n):
            if digits[i] < digits[max_idx[i]]:
                digits[i], digits[max_idx[i]] = digits[max_idx[i]], digits[i]
                break

        result = 0
        for digit in digits:
            result = result * 10 + digit

        return result


s = Solution()
print(s.maximumSwap(2736))
print(s.maximumSwap(9973))
