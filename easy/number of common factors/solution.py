class Solution:
    def commonFactors(self, a, b):
        while b:
            a, b = b, a % b
        result = 1
        div = 2
        while a != 1 and div * div <= a:
            count = 0
            while a % div == 0:
                count += 1
                a //= div
            result *= count + 1
            div += 1
        if a != 1:
            result *= 2
        return result

    def commonFactors1(self, a: int, b: int) -> int:
        m = min(a, b)
        result = 0
        for i in range(1, m + 1):
            if a % i == 0 and b % i == 0:
                result += 1
        return result


s = Solution()

print(s.commonFactors(12, 6))
print(s.commonFactors(25, 30))
print(s.commonFactors(885, 885))
