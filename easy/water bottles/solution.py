class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)

    def numWaterBottles1(self, numBottles: int, numExchange: int) -> int:
        result = 0
        while numBottles >= numExchange:
            result += numExchange
            numBottles -= numExchange
            numBottles += 1
        return result + numBottles


s = Solution()
print(s.numWaterBottles(9, 3))
print(s.numWaterBottles(15, 4))
print(s.numWaterBottles(15, 10))
