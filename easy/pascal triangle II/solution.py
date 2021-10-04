from typing import List


class Solution:
    def getRow2(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        result = []
        temp = self.getRow2(rowIndex - 1)
        n = len(temp)
        for i in range(n - 1):
            result.append(temp[i] + temp[i + 1])
        return [1] + result + [1]

    def getRow1(self, rowIndex: int) -> List[int]:
        row = [1]
        triangle = []
        for i in range(rowIndex + 1):
            triangle.append(row)
            row = [sum(x) for x in zip([0] + row, row + [0])]
        return triangle[rowIndex]


s = Solution()
print(s.getRow1(3))
print(s.getRow1(0))
print(s.getRow1(1))
print(s.getRow1(33))
print(s.getRow2(3))
print(s.getRow2(0))
print(s.getRow2(1))
print(s.getRow2(33))
