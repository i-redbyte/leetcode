class Solution:
    def tribonacci(self, n: int) -> int:
        def fib(m: int) -> int:
            if m == 0:
                return 0
            if m == 1:
                return 1
            if m == 2:
                return 1
            return fib(m-1) + fib(m - 2) + fib(m - 3)
        return fib(n)


s = Solution()
print(s.tribonacci(4))
print(s.tribonacci(5))
print(s.tribonacci(6))
print(s.tribonacci(10))
print(s.tribonacci(11))
print(s.tribonacci(25))
