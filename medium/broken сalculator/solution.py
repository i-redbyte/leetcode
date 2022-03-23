class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if target <= startValue:
            return startValue - target
        result = 0
        while target > startValue:
            if target & 1:
                target += 1
                result += 1
            target >>= 1
            result += 1
        result += startValue - target
        return result

    def brokenCalc1(self, startValue: int, target: int) -> int:
        result = 0
        while target > startValue:
            result += 1
            if target & 1 != 0:
                target += 1
            else:
                target //= 2
        return result + startValue - target


print(Solution().brokenCalc(2, 3))
print(Solution().brokenCalc(5, 8))
print(Solution().brokenCalc(3, 10))
