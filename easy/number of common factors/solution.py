class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        m = max(a, b)
        result = 0
        for i in range(1, m+1):
            if a % i == 0 and b % i == 0:
                result += 1
        return result


s = Solution()

print(s.commonFactors(12, 6))
print(s.commonFactors(25, 30))
print(s.commonFactors(885, 885))
