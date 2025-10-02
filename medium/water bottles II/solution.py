class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
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
