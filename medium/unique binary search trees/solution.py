class Solution:
    def fak(self, n):
        if n == 1:
            return 1
        return self.fak(n - 1) * n

    def numTrees(self, n: int) -> int:
        return self.fak((2 * n)) // (self.fak(n) * self.fak(n + 1))


s = Solution()
print(s.numTrees(3))
print(s.numTrees(1))
print(s.numTrees(19))
