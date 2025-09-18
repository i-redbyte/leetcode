class Solution:
    def kthCharacter(self, k: int) -> str:
        x = k - 1
        cnt = 0
        while x:
            x &= x - 1
            cnt += 1
        return chr(ord('a') + (cnt % 26))


s = Solution()
print(s.kthCharacter(5))
print(s.kthCharacter(10))
print(s.kthCharacter(1))
