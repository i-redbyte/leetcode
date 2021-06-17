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
print(s.sumBase(10, 9))
print(s.sumBase(7, 2))
print(s.sumBase(255, 2))
print(s.sumBase(999, 10))
print(s.sumBase(3, 3))
print(s.sumBase(88, 8))
print(s.sumBase(777, 7))
print(s.sumBase(1024, 4))
