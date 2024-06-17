
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 2
        while i * i <= c:
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c /= i
                if i % 4 == 3 and count % 2 != 0:
                    return False
            i += 1
        return c % 4 != 3


s = Solution()
print(s.judgeSquareSum(5))
print(s.judgeSquareSum(3))
print(s.judgeSquareSum(6))
print(s.judgeSquareSum(8))
