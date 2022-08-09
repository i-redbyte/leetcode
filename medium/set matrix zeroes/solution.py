from typing import List


class Solution:
    def print(self, matrix: List[List[int]]) -> None:
        print()
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in matrix]))

    def setZeroes(self, matrix: List[List[int]]) -> None:
        self.print(matrix)
        firstCol = False
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            if matrix[i][0] == 0:
                firstCol = True
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        if firstCol:
            for i in range(n):
                matrix[i][0] = 0
        self.print(matrix)
        return

    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # self.print(matrix)
        n = len(matrix)
        m = len(matrix[0])
        rows = []
        cols = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        # self.print(matrix)


Solution().setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
