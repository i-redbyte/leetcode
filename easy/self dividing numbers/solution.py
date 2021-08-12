from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right + 1):
            if self.isSelfDividingNumbers(i):
                result.append(i)
        return result

    def isSelfDividingNumbers(self, x: int) -> bool:
        value = x
        if x <= 9:
            return True
        while x != 0:
            n = x % 10
            if n == 0 or value % n != 0:
                return False
            x //= 10
        return True


s = Solution()
print(s.selfDividingNumbers(1, 22))
print(s.selfDividingNumbers(22, 1))
print(s.selfDividingNumbers(127, 128))
