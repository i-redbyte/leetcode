class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 * num2 == 0:
            return 0
        return num1 // num2 + self.countOperations(num2, num1 % num2)

    def countOperations1(self, num1: int, num2: int) -> int:
        result = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            result += 1
        return result


s = Solution()
print(s.countOperations(2, 3))
print(s.countOperations(10, 10))
