class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n & 1 == 0:
            return n
        return n << 1


s = Solution()
print(s.smallestEvenMultiple(5))
print(s.smallestEvenMultiple(6))
