class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        r = 1
        for i in range(1, k + 1):
            if r % k == 0:
                return i
            r = (r * 10 + 1) % k
        return -1


s = Solution()
print(s.smallestRepunitDivByK(1))
print(s.smallestRepunitDivByK(2))
print(s.smallestRepunitDivByK(3))
