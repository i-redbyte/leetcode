class Solution:
    mem = [0] * 38

    def tribonacci(self, n: int) -> int:
        if self.mem[n] != 0:
            return self.mem[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        self.mem[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.mem[n]

    def tribonacci2(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        tribonacci = [0] * (n + 1)
        tribonacci[0] = 0
        tribonacci[1] = 1
        tribonacci[2] = 1
        for i in range(3, n + 1):
            tribonacci[i] = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3]
        return tribonacci[n]

    def tribonacci1(self, n: int) -> int:
        def fib(m: int) -> int:
            if m == 0:
                return 0
            if m == 1:
                return 1
            if m == 2:
                return 1
            return fib(m - 1) + fib(m - 2) + fib(m - 3)

        return fib(n)


s = Solution()
print(s.tribonacci(4))
print(s.tribonacci(5))
print(s.tribonacci(6))
print(s.tribonacci(10))
print(s.tribonacci(11))
print(s.tribonacci(25))
print(s.tribonacci(30))
