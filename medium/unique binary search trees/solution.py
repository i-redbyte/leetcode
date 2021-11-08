class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        v = [0] * (n + 1)
        v[0], v[1], v[2] = 1, 1, 2
        for i in range(2, n):
            for j in range(0, i+1):
                v[i + 1] += v[j] * v[i - j]
        return v[n]

    def fak(self, n):
        if n == 1:
            return 1
        return self.fak(n - 1) * n

    def numTrees1(self, n: int) -> int:
        return self.fak((2 * n)) // (self.fak(n) * self.fak(n + 1))


s = Solution()
print(s.numTrees(3))
print(s.numTrees(1))
print(s.numTrees(19))
