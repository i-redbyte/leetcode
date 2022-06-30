class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count('1')

    def minBitFlips1(self, start: int, goal: int) -> int:
        condition = start ^ goal
        result = 0
        while condition > 0:
            condition = condition & (condition - 1)
            result += 1
        return result


print(Solution().minBitFlips(start=10, goal=7))
print(Solution().minBitFlips(3, 4))
