import math


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        E = numBottles
        X = numExchange

        a = 1
        b = 2 * X - 3
        c = 2 * (1 - E)

        D = b * b - 4 * a * c
        sqrtD = math.isqrt(D)

        k = (-b + sqrtD) // 2
        if k < 0:
            k = 0

        def ok(t: int) -> bool:
            return t * t + (2 * X - 3) * t + 2 * (1 - E) <= 0

        while ok(k + 1):
            k += 1
        while k > 0 and not ok(k):
            k -= 1

        return E + k

    def maxBottlesDrunk1(self, numBottles: int, numExchange: int) -> int:
        total_drunk = 0
        empty_bottles = 0
        current_exchange = numExchange

        while numBottles > 0:
            total_drunk += numBottles
            empty_bottles += numBottles
            numBottles = 0

            while empty_bottles >= current_exchange:
                numBottles += 1
                empty_bottles -= current_exchange
                current_exchange += 1

        return total_drunk


s = Solution()
print(s.maxBottlesDrunk(13, 6))
print(s.maxBottlesDrunk(10, 3))
