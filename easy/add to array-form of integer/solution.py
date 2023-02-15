from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = 0
        n = len(num) - 1
        for i, v in enumerate(num):
            s += v * (10 ** (n - i))
        s += k
        result = []
        while s != 0:
            result.append(s % 10)
            s //= 10
        return result[::-1]


s = Solution()
print(s.addToArrayForm(num=[1], k=34))
print(s.addToArrayForm(num=[1, 2, 0, 0], k=34))
print(s.addToArrayForm(num=[2, 7, 4], k=181))
print(s.addToArrayForm(num=[2, 1, 5], k=806))
