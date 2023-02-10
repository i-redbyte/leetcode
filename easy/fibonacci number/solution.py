class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))
print(s.fib(5))
