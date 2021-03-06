from math import log2


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        result = int(log2(num))
        while num > 0:
            result += 1
            num &= num - 1
        return result


def numberOfSteps2(self, num: int) -> int:
    digits = f'{num:b}'
    return digits.count('1') - 1 + len(digits)


def numberOfSteps1(self, num: int) -> int:
    steps = 0
    while num > 0:
        if num & 1 == 0:
            num = num // 2
        else:
            num -= 1
        steps += 1
    return steps


s = Solution()
print(s.numberOfSteps(14))
print(s.numberOfSteps(8))
print(s.numberOfSteps(123))
