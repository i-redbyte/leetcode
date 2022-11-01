class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while n > 0:
            m = n % 10
            n = n // 10
            s += m
            p *= m
        return p - s


s = Solution()
print(s.subtractProductAndSum(234))
print(s.subtractProductAndSum(4421))
