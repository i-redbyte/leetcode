class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def recursion(n: int, k: int) -> int:
            if n == 1:
                return 0
            return (recursion(n - 1, k) + k) % n
        return recursion(n, k) + 1


s = Solution()
print(s.findTheWinner(n=5, k=2))
print(s.findTheWinner(n=6, k=5))
