from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        triangle = []
        for i in range(34):
            triangle.append(row)
            row = [sum(x) for x in zip([0] + row, row + [0])]
        return triangle[rowIndex]


s = Solution()
print(s.getRow(3))
print(s.getRow(0))
print(s.getRow(1))
print(s.getRow(33))
