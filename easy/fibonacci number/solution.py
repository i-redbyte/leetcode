class Solution:
    def fib1(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

    def fib2(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        f1 = 0
        f2 = 1
        result = 0
        for i in range(1, n):
            result = f1 + f2
            f1 = f2
            f2 = result
        return result

    def fib(self, n: int) -> int:
        def solution(n: int, f1: int = 0, f2: int = 1) -> int:
            if n == 0:
                return f1
            if n == 1:
                return f2
            return solution(n - 1, f2, f1 + f2)
        return solution(n)


s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))
print(s.fib(5))
