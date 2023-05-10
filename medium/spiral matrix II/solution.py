import math
from typing import List


def printMatrix(matrix: List[List[int]]):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        counter, row, col = 1, 0, 0

        while counter <= n ** 2:
            while row < n and matrix[col][row] == 0:
                matrix[col][row] = counter
                row += 1 if row != n - 1 and matrix[col][row + 1] == 0 else 0
                counter += 1
            col += 1

            while col < n and matrix[col][row] == 0:
                matrix[col][row] = counter
                col += 1 if col != n - 1 and matrix[col + 1][row] == 0 else 0
                counter += 1
            row -= 1

            while row >= 0 and matrix[col][row] == 0:
                matrix[col][row] = counter
                row -= 1 if row != 0 and matrix[col][row - 1] == 0 else 0
                counter += 1
            col -= 1

            while col >= 0 and matrix[col][row] == 0:
                matrix[col][row] = counter
                col -= 1 if col != 0 and matrix[col - 1][row] == 0 else 0
                counter += 1
            row += 1

        return matrix


s = Solution()
printMatrix(s.generateMatrix(3))
printMatrix(s.generateMatrix(10))
