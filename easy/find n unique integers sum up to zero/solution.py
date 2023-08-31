from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [0] * n
        i = 0
        j = n - 1
        mid = n // 2
        while i < j:
            result[i] = mid * (-1)
            result[j] = mid
            mid -= 1
            j -= 1
            i += 1
        return result


s = Solution()
print(s.sumZero(5))
print(s.sumZero(3))
print(s.sumZero(1))
