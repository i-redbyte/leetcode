import math


class Solution:
    def minSwaps(self, c: str) -> int:
        n = len(c)
        num_zero = c.count("0")
        num_one = n - num_zero
        if abs(num_zero - num_one) > 1:
            return -1
        c = int(c, base=2)
        num_alternations = math.ceil(n / 2)
        alternating_0 = int('10' * num_alternations, base=2)
        alternating_1 = int('01' * num_alternations, base=2)
        zero_count = bin(c ^ alternating_0).count("1")
        one_count = bin(c ^ alternating_1).count("1")
        if num_zero > num_one:
            count_to_use = zero_count
        elif num_one > num_zero:
            count_to_use = one_count
        else:
            count_to_use = min(zero_count, one_count)
        return count_to_use // 2


s = Solution()
print(s.minSwaps("111000"))
print(s.minSwaps("010"))
print(s.minSwaps("1110"))
