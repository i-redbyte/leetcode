import pprint
from typing import List


class Solution:
    def printMatrix(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in matrix]))

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))

    def transpose1(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        result = [[0 for x in range(row)] for y in range(col)]
        n = len(result)
        m = len(result[0])
        for i in range(n):
            for j in range(m):
                result[i][j] = matrix[j][i]
        # self.printMatrix(matrix)
        # print()
        # self.printMatrix(result)
        return result


s = Solution()
print(s.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.transpose([[1, 2, 3], [4, 5, 6]]))
