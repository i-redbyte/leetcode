import math


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        result = 1
        c = 1
        while n > 0:
            n -= 1
            tmp = result + c
            result = c
            c = tmp
        return result

    # Solution 2
    # Use  Fibonacci Formula
    def climbStairs2(self, n: int) -> int:
        s = math.sqrt(5)
        n_fib = pow((1 + s) / 2, n + 1) - pow((1 - s) / 2, n + 1)
        return int(n_fib / s)


s = Solution()
# print(s.climbStairs(2))
# print(s.climbStairs(3))
# print(s.climbStairs(4))
# print(s.climbStairs(10))
# print(s.climbStairs(45))

print(s.climbStairs2(2))
print(s.climbStairs2(3))
print(s.climbStairs2(4))
print(s.climbStairs2(5))
print(s.climbStairs2(6))
print(s.climbStairs2(9))
print(s.climbStairs2(10))
print(s.climbStairs2(45))
