from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        triangle = []
        for i in range(numRows):
            triangle.append(row)
            row = [sum(x) for x in zip([0] + row, row + [0])]
        return triangle


s = Solution()
print(s.generate(1))
print(s.generate(5))
print(s.generate(7))
print(s.generate(30))
print(s.generate(10))
