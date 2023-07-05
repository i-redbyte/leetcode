from math import log2


class Solution:
    def change_zero_bit(self, b: int) -> int:
        return (1 << b + 1) - 1

    def change_int_n_bit(self, n: int) -> int:
        if n == 0:
            return 0
        b1 = int(log2(n))
        return self.change_zero_bit(b1) - self.change_int_n_bit(n - (1 << b1))

    def minimumOneBitOperations(self, n: int) -> int:
        return self.change_int_n_bit(n)


s = Solution()
print(s.minimumOneBitOperations(3))
print(s.minimumOneBitOperations(6))
