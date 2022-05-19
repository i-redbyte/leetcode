class Solution:
    def countEven(self, num: int) -> int:
        result = 0
        for i in range(1, num + 1):
            acc = self.get_digits_sum(i)
            if acc & 1 == 0:
                result += 1
        return result

    def get_digits_sum(self, num):
        acc = 0
        while num > 0:
            acc += num % 10
            num = num // 10
        return acc


s = Solution()
print(s.countEven(4))
print(s.countEven(30))
