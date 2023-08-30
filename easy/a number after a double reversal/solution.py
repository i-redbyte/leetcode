class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def reverse(x: int) -> int:
            result = 0
            z = x
            p = 0
            while z > 0:
                if p == 0:
                    p = 1
                else:
                    p *= 10
                z = z // 10

            while x > 0:
                result += (x % 10) * p
                p //= 10
                x = x // 10
            return result
        return reverse(reverse(num)) == num


s = Solution()
print(s.isSameAfterReversals(526))
print(s.isSameAfterReversals(1800))
print(s.isSameAfterReversals(0))
