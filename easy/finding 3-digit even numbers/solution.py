from typing import List
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        result = []
        for n in range(100, 1000, 2):
            a = n // 100
            b = (n // 10) % 10
            c = n % 10
            need = Counter((a, b, c))
            if all(freq[d] >= cnt for d, cnt in need.items()):
                result.append(n)
        return result


s = Solution()
print(s.findEvenNumbers([2, 1, 3, 0]))
print(s.findEvenNumbers([2, 2, 8, 8, 2]))
print(s.findEvenNumbers([3, 7, 5]))
