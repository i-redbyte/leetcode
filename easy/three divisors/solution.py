class Solution:
    def isThree(self, n: int) -> bool:
        count_divisors = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count_divisors += 1
        return count_divisors == 3


s = Solution()
print(s.isThree(2))
print(s.isThree(4))
print(s.isThree(12))
print(s.isThree(9))
