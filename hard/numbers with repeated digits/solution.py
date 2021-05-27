class Solution:
    def point(self, n, k):
        if k == 0:
            return 1
        return n * self.point(n - 1, k - 1)

    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        digits_n = len(digits)
        if digits_n < 2:
            return 0
        result = 0
        for k in range(digits_n - 1):
            result += 9 * self.point(9, k)
        result += (digits[0] - 1) * self.point(9, digits_n - 1)
        selected = {digits[0]}
        i = 1
        for d in digits[1:]:
            i += 1
            select_n = d - sum(x < d for x in selected)
            result += select_n * self.point(10 - i, digits_n - i)
            if d in selected:
                break
            selected.add(d)
        else:
            result += 1
        return n - result


s = Solution()
print(s.numDupDigitsAtMostN(20))
print(s.numDupDigitsAtMostN(100))
print(s.numDupDigitsAtMostN(1000))
