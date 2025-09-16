class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if (k & ~n) != 0:
            return -1

        x = n ^ k
        cnt = 0
        while x:
            x &= x - 1
            cnt += 1
        return cnt


s = Solution()
print(s.minChanges(13, 4))
print(s.minChanges(21, 21))
print(s.minChanges(14, 13))
