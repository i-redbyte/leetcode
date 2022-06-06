class Solution:
    def minimumSum(self, num: int) -> int:
        numbers = []
        while num > 0:
            numbers.append(num % 10)
            num = num // 10
        numbers.sort()
        return 10 * (numbers[0] + numbers[1]) + numbers[2] + numbers[3]


s = Solution()
print(s.minimumSum(2932))
print(s.minimumSum(4009))
