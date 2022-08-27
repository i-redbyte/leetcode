from typing import List


class Solution:

    def count(self, n: int) -> List[int]:
        result = [0] * 10
        while n > 0:
            result[n % 10] += 1
            n //= 10
        return result

    def reorderedPowerOf2(self, n: int) -> bool:
        arr = self.count(n)
        for i in range(31):
            if arr == self.count(1 << i):
                return True
        return False


print(Solution().reorderedPowerOf2(1))
print(Solution().reorderedPowerOf2(10))
