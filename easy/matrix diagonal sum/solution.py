from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        n = len(mat)
        for i in range(0, n):
            result += mat[i][i]
            if i != n - i - 1:
                result += mat[n - i - 1][i]
        return result


s = Solution()
print(s.diagonalSum([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]))
print(s.diagonalSum([[1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1]]))
print(s.diagonalSum([[5]]))
