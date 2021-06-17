class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = 0
        while n > 0:
            result += n % k
            n = n // k
        return result


s = Solution()
print(s.sumBase(34, 6))
print(s.sumBase(10, 10))
print(s.sumBase(10, 1))
